import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, now_datetime


class CCPayment(Document):
	def validate(self):
		# Kunde + Betrag aus der Rechnung übernehmen, falls leer
		if self.invoice:
			inv = frappe.db.get_value(
				"CC Invoice", self.invoice, ["customer", "amount_total"], as_dict=True
			)
			if inv:
				if not self.customer:
					self.customer = inv.customer
				if not self.amount:
					self.amount = inv.amount_total

		if self.status == "Bezahlt" and not self.paid_at:
			self.paid_at = now_datetime()

	def on_update(self):
		"""Bezahlte Zahlung markiert die verknüpfte Rechnung als 'Bezahlt'."""
		if self.status == "Bezahlt" and self.invoice:
			current = frappe.db.get_value("CC Invoice", self.invoice, "status")
			if current != "Bezahlt":
				inv = frappe.get_doc("CC Invoice", self.invoice)
				inv.status = "Bezahlt"
				inv.save(ignore_permissions=True)
				frappe.msgprint(
					_("Rechnung {0} wurde als bezahlt markiert.").format(self.invoice),
					alert=True,
					indicator="green",
				)

	# --- Stripe-Anbindung ---------------------------------------------------
	# Keys liegen in der Server-Config (frappe.conf.stripe_secret_key / _webhook_secret)
	# – NIEMALS im öffentlichen Repo. Wird in der Integrationsphase scharf geschaltet.
	@frappe.whitelist()
	def create_checkout_session(self):
		"""Stripe-Checkout-Session für diese Zahlung erstellen (später aktiv)."""
		# TODO Stripe: stripe.checkout.Session.create(
		#   mode="payment", line_items=[{amount: self.amount*100, currency: "eur", ...}],
		#   payment_method_types=["card", "sepa_debit"],
		#   success_url=..., cancel_url=...)
		#   -> self.db_set("stripe_checkout_session", session.id); return session.url
		frappe.msgprint(
			_("Stripe ist noch nicht aktiviert (folgt in der Integrationsphase mit echten Keys)."),
			alert=True,
			indicator="orange",
		)


@frappe.whitelist(allow_guest=True)
def stripe_webhook():
	"""Platzhalter-Endpunkt für Stripe-Webhooks (checkout.session.completed etc.).
	Signaturprüfung mit frappe.conf.stripe_webhook_secret folgt in der
	Integrationsphase. Aktuell ohne Funktion."""
	# TODO Stripe: Event verifizieren -> zugehörige CC Payment auf 'Bezahlt' setzen
	return {"received": True}
