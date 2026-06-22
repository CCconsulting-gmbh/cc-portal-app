import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class CCBooking(Document):
	def validate(self):
		# Preis aus der Leistung übernehmen, falls noch leer
		if self.service and not self.price:
			self.price = frappe.db.get_value("CC Service", self.service, "price")

	def on_update(self):
		"""Wenn eine Buchung 'Erledigt' ist: Treuepunkte gutschreiben und einen
		Rechnungsentwurf erzeugen (jeweils nur einmal, über Flags abgesichert)."""
		if self.status == "Erledigt":
			self.award_loyalty_points()
			self.create_invoice_if_needed()

	def award_loyalty_points(self):
		if self.points_awarded or not self.service:
			return
		points = frappe.db.get_value("CC Service", self.service, "loyalty_points")
		if not points:
			return
		try:
			frappe.get_doc(
				{
					"doctype": "CC Loyalty Transaction",
					"customer": self.customer,
					"transaction_type": "Gutschrift",
					"points": int(points),
					"reason": f"Buchung {self.name}",
					"reference": self.name,
				}
			).insert(ignore_permissions=True)
			self.db_set("points_awarded", 1)
			frappe.msgprint(
				_("{0} Treuepunkte gutgeschrieben.").format(int(points)),
				alert=True,
				indicator="green",
			)
		except Exception:
			frappe.log_error(
				frappe.get_traceback(), "CC Portal: Loyalty-Gutschrift (Buchung) fehlgeschlagen"
			)

	def create_invoice_if_needed(self):
		if self.invoice or flt(self.price) <= 0:
			return
		try:
			inv = frappe.get_doc(
				{
					"doctype": "CC Invoice",
					"customer": self.customer,
					"status": "Entwurf",
					"amount_net": flt(self.price),
					"notes": f"Automatisch aus Buchung {self.name}",
				}
			)
			inv.insert(ignore_permissions=True)
			self.db_set("invoice", inv.name)
			frappe.msgprint(
				_("Rechnungsentwurf {0} erstellt.").format(inv.name),
				alert=True,
				indicator="green",
			)
		except Exception:
			frappe.log_error(
				frappe.get_traceback(), "CC Portal: Auto-Rechnung (Buchung) fehlgeschlagen"
			)
