import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import now_datetime


class CCDocument(Document):
	def before_insert(self):
		# Eindeutiges Token für die spätere Kunden-Signatur im Portal
		if not self.signature_token:
			self.signature_token = frappe.generate_hash(length=32)

	def validate(self):
		# Beim Setzen auf 'Signiert' den Zeitstempel füllen
		if self.status == "Signiert" and not self.signed_at:
			self.signed_at = now_datetime()
		# Zurücksetzen auf Entwurf löscht die Signaturspuren
		if self.status in ("Entwurf", "Zur Signatur"):
			self.signed_at = None

	@frappe.whitelist()
	def mark_signed(self, signer_name=None, signature_image=None):
		"""Dokument als signiert markieren (intern oder später vom Portal aufgerufen)."""
		self.signed_by_name = signer_name or frappe.session.user
		if signature_image:
			self.signature_image = signature_image
		self.signed_at = now_datetime()
		self.status = "Signiert"
		self.save(ignore_permissions=True)
		frappe.msgprint(_("Dokument wurde als signiert markiert."), alert=True, indicator="green")
		return self.name
