"""Demo-Daten für das CC Portal.

Ausführen auf dem Server:
    bench --site <site> execute cc_portal.demo.seed_demo

Idempotent: legt fehlende Datensätze an, lässt vorhandene unberührt.
"""

import frappe
from frappe.utils import add_days, nowdate


CUSTOMER = "Mustermann GmbH"


def _ensure_customer():
	if frappe.db.exists("HD Customer", CUSTOMER):
		return CUSTOMER
	doc = frappe.get_doc({"doctype": "HD Customer", "name": CUSTOMER})
	# Feldname variiert je nach Helpdesk-Version – defensiv setzen
	for field in ("customer_name", "customer"):
		if doc.meta.has_field(field):
			doc.set(field, CUSTOMER)
	doc.insert(ignore_permissions=True)
	return doc.name


def _get_or_create(doctype, filters, values):
	name = frappe.db.get_value(doctype, filters)
	if name:
		return name
	doc = frappe.get_doc({"doctype": doctype, **values})
	doc.insert(ignore_permissions=True)
	return doc.name


def seed_demo():
	customer = _ensure_customer()

	# --- Leistungen (Modul 4) ---------------------------------------------
	svc_web = _get_or_create(
		"CC Service",
		{"service_name": "Website-Wartung"},
		{"service_name": "Website-Wartung", "price": 150, "duration_minutes": 60,
		 "loyalty_points": 15, "active": 1, "description": "Monatliche Pflege & Updates"},
	)
	_get_or_create(
		"CC Service",
		{"service_name": "SEO-Beratung"},
		{"service_name": "SEO-Beratung", "price": 500, "duration_minutes": 120,
		 "loyalty_points": 50, "active": 1, "description": "Analyse + Maßnahmenplan"},
	)

	# --- Projekt + Briefing (Modul 1) -------------------------------------
	project = _get_or_create(
		"CC Project",
		{"project_name": "Website Relaunch Mustermann"},
		{"project_name": "Website Relaunch Mustermann", "customer": customer,
		 "status": "Planung", "progress": 20},
	)
	if not frappe.db.exists("CC Briefing", {"project": project}):
		frappe.get_doc({
			"doctype": "CC Briefing",
			"project": project,
			"goal": "Neue Firmenwebsite mit Terminbuchung",
			"scope": "5 Seiten, Kontaktformular, Design nach CI",
			"budget": "8.000 €",
			"deadline": add_days(nowdate(), 60),
			"completed": 0,
		}).insert(ignore_permissions=True)

	# --- Rechnung (Modul 2) -----------------------------------------------
	invoice = _get_or_create(
		"CC Invoice",
		{"customer": customer, "notes": "Demo-Rechnung"},
		{"customer": customer, "project": project, "status": "Offen",
		 "issue_date": nowdate(), "due_date": add_days(nowdate(), 14),
		 "amount_net": 1000, "tax_rate": 19, "notes": "Demo-Rechnung"},
	)

	# --- Buchung (Modul 4 -> Loyalty + Auto-Rechnung) ---------------------
	if not frappe.db.exists("CC Booking", {"customer": customer, "service": svc_web}):
		frappe.get_doc({
			"doctype": "CC Booking",
			"customer": customer,
			"service": svc_web,
			"status": "Erledigt",  # löst Punkte + Rechnungsentwurf aus
			"booking_date": nowdate(),
		}).insert(ignore_permissions=True)

	# --- Zusätzliche Treuepunkte (Modul 3) --------------------------------
	if not frappe.db.exists("CC Loyalty Transaction", {"customer": customer, "reason": "Willkommensbonus"}):
		frappe.get_doc({
			"doctype": "CC Loyalty Transaction",
			"customer": customer,
			"transaction_type": "Gutschrift",
			"points": 500,
			"reason": "Willkommensbonus",
		}).insert(ignore_permissions=True)

	# --- Prämie (Modul 3) -------------------------------------------------
	_get_or_create(
		"CC Loyalty Reward",
		{"reward_name": "1 Stunde Beratung gratis"},
		{"reward_name": "1 Stunde Beratung gratis", "points_cost": 300, "active": 1,
		 "description": "Einlösbar für eine kostenlose Beratungsstunde"},
	)

	# --- Dokument (Modul 5) -----------------------------------------------
	_get_or_create(
		"CC Document",
		{"title": "Wartungsvertrag Mustermann"},
		{"title": "Wartungsvertrag Mustermann", "customer": customer, "project": project,
		 "document_type": "Vertrag", "status": "Zur Signatur", "requires_signature": 1},
	)

	# --- Zahlung (Modul 8 -> Rechnung bezahlt) ----------------------------
	if invoice and not frappe.db.exists("CC Payment", {"invoice": invoice}):
		frappe.get_doc({
			"doctype": "CC Payment",
			"invoice": invoice,
			"status": "Bezahlt",
			"method": "Kreditkarte",
		}).insert(ignore_permissions=True)

	# --- Wissensartikel (Modul 7) -----------------------------------------
	_get_or_create(
		"CC Knowledge",
		{"title": "Strato-Postfach einrichten"},
		{"title": "Strato-Postfach einrichten", "category": "Anleitung",
		 "visibility": "Intern", "published": 1,
		 "content": "<p>1. Im Strato-Kundenbereich anmelden …</p>"},
	)

	frappe.db.commit()
	print("✅ Demo-Daten angelegt für Kunde:", customer)
