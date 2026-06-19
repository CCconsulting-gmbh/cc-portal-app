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

# Spätere Module hängen hier Geschäftslogik ein:
# doc_events = { "CC Project": { "validate": "cc_portal.cc_portal.doctype.cc_project.cc_project.validate" } }
# scheduler_events = { ... }
