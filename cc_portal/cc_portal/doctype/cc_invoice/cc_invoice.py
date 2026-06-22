import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate, nowdate


class CCInvoice(Document):
	def validate(self):
		self.calculate_totals()
		self.apply_status_rules()

	def calculate_totals(self):
		"""MwSt + Bruttosumme immer aus Netto + Satz neu berechnen."""
		net = flt(self.amount_net)
		rate = flt(self.tax_rate)
		self.amount_tax = round(net * rate / 100.0, 2)
		self.amount_total = round(net + self.amount_tax, 2)

	def apply_status_rules(self):
		"""Geschäftsregeln:
		- 'Bezahlt' setzt automatisch das Bezahldatum (falls leer).
		- Eine 'Offen'e Rechnung wird 'Überfällig', wenn das Fälligkeitsdatum
		  überschritten ist."""
		if self.status == "Bezahlt" and not self.paid_date:
			self.paid_date = nowdate()

		if (
			self.status == "Offen"
			and self.due_date
			and getdate(self.due_date) < getdate(nowdate())
		):
			self.status = "Überfällig"

	# --- Bitrix24-Anbindung -------------------------------------------------
	# crm.item.* mit entityTypeId 31 (Rechnungen). Zugangsdaten/Webhook-URL
	# kommen aus der Frappe-Konfiguration (NICHT ins öffentliche Repo!).
	@frappe.whitelist()
	def sync_to_bitrix(self):
		"""Rechnung nach Bitrix24 spiegeln. Wird später scharf geschaltet."""
		# TODO Bitrix24: REST-Call crm.item.add / crm.item.update (entityTypeId=31)
		#   - Webhook-Basis-URL aus site_config (frappe.conf.bitrix_webhook_url)
		#   - bei Erfolg self.db_set("bitrix_invoice_id", <id>)
		frappe.msgprint(
			_("Bitrix24-Sync ist noch nicht aktiviert (folgt in der Integrationsphase)."),
			alert=True,
			indicator="orange",
		)
