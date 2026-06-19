import frappe

no_cache = 1


def get_context(context):
	"""Liefert die Boot-Daten für die CC-Portal-SPA. Login läuft über die
	normale Frappe-Session (Cookie) – Gäste werden zum Login geschickt."""
	if frappe.session.user == "Guest":
		frappe.local.flags.redirect_location = "/login?redirect-to=/cc-portal"
		raise frappe.Redirect

	frappe.db.commit()
	context.csrf_token = frappe.sessions.get_csrf_token()
	context.site_name = frappe.local.site
	context.boot = {
		"lang": frappe.local.lang or "de",
		"dir": "rtl" if (frappe.local.lang or "") in ("ar", "he") else "ltr",
		"user": frappe.session.user,
		"sitename": frappe.local.site,
	}
	return context
