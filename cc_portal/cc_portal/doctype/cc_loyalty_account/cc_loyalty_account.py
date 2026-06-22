import frappe
from frappe.model.document import Document
from frappe.utils import flt


# Stufen-Schwellen nach Lifetime-Punkten
TIERS = [(5000, "Platin"), (2000, "Gold"), (500, "Silber"), (0, "Bronze")]


def tier_for(lifetime_points):
	for threshold, name in TIERS:
		if flt(lifetime_points) >= threshold:
			return name
	return "Bronze"


def get_or_create_account(customer):
	"""Liefert den Kontonamen für einen Kunden – legt das Konto bei Bedarf an."""
	name = frappe.db.get_value("CC Loyalty Account", {"customer": customer}, "name")
	if name:
		return name
	account = frappe.get_doc({"doctype": "CC Loyalty Account", "customer": customer})
	account.insert(ignore_permissions=True)
	return account.name


def recompute(account, exclude_txn=None):
	"""Punktestand + Lifetime + Stufe sauber aus allen Transaktionen neu berechnen.
	`exclude_txn` lässt eine (gerade zu löschende) Transaktion außen vor."""
	filters = {"account": account}
	rows = frappe.get_all(
		"CC Loyalty Transaction", filters=filters, fields=["name", "points"]
	)
	balance = 0
	lifetime = 0
	for r in rows:
		if exclude_txn and r.name == exclude_txn:
			continue
		pts = flt(r.points)
		balance += pts
		if pts > 0:
			lifetime += pts
	frappe.db.set_value(
		"CC Loyalty Account",
		account,
		{
			"points_balance": int(balance),
			"lifetime_points": int(lifetime),
			"tier": tier_for(lifetime),
		},
	)


class CCLoyaltyAccount(Document):
	pass
