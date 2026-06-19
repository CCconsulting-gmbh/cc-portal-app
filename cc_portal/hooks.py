app_name = "cc_portal"
app_title = "CC Portal"
app_publisher = "CC Consulting GmbH"
app_description = "CC Consulting Portal-Features auf Frappe Helpdesk"
app_email = "info@cc-consulting.gmbh"
app_license = "mit"

# Unsere Rollen werden als Fixtures mit der App ausgeliefert (cc_portal/fixtures/role.json)
fixtures = [
    {
        "dt": "Role",
        "filters": [["role_name", "in", ["CC Vertrieb", "CC IT", "CC Buchhalter", "CC Manager"]]],
    },
]

# Schicke SPA-Oberfläche: alle /cc-portal/* URLs an die www/cc_portal-Seite leiten,
# damit das clientseitige Vue-Routing funktioniert.
website_route_rules = [
    {"from_route": "/cc-portal", "to_route": "cc_portal"},
    {"from_route": "/cc-portal/<path:app_path>", "to_route": "cc_portal"},
]

# Spätere Module hängen hier Geschäftslogik ein:
# doc_events = { ... }
# scheduler_events = { ... }
