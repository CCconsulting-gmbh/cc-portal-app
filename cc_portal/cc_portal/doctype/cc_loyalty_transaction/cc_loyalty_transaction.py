import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt

from cc_portal.cc_portal.doctype.cc_loyalty_account.cc_loyalty_account import (
	get_or_create_account,
	recompute,
)


class CCLoyaltyTransaction(Document):
	def validate(self):
		# Konto immer aus dem Kunden auflösen (bei Bedarf anlegen)
		if self.customer and not self.account:
			self.account = get_or_create_account(self.customer)

		# Einlösung darf den Punktestand nicht ins Minus drücken
		if flt(self.points) < 0:
			balance = flt(
				frappe.db.get_value("CC Loyalty Account", self.account, "points_balance")
			)
			# bestehende Buchung (beim Bearbeiten) herausrechnen
			if not self.is_new():
				old = flt(frappe.db.get_value(self.doctype, self.name, "points"))
				balance -= old
			if balance + flt(self.points) < 0:
				frappe.throw(
					_("Nicht genug Punkte: Kontostand {0}, Einlösung {1}.").format(
						int(balance), int(self.points)
					)
				)

	def on_update(self):
		recompute(self.account)

	def after_insert(self):
		recompute(self.account)

	def on_trash(self):
		# Diese Transaktion beim Neuberechnen ausschließen (wird gerade gelöscht)
		if self.account:
			recompute(self.account, exclude_txn=self.name)
