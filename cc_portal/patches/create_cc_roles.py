import frappe

ROLES = ["CC Vertrieb", "CC IT", "CC Buchhalter", "CC Manager"]


def execute():
	"""Legt unsere Rollen an, bevor DocTypes mit Rechten auf diese Rollen synchronisiert werden.
	Läuft als pre_model_sync-Patch, damit die Rollen-Links in den DocType-Berechtigungen gültig sind.
	Idempotent."""
	for role_name in ROLES:
		if not frappe.db.exists("Role", role_name):
			frappe.get_doc(
				{"doctype": "Role", "role_name": role_name, "desk_access": 1}
			).insert(ignore_permissions=True)
