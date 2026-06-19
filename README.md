# CC Portal (Frappe-App)

Eigene Frappe-App von **CC Consulting GmbH** mit den Portal-Features (Projekte, Briefing-Workflow,
Rechnungen, Loyalty, Buchung, Dokumente/Signatur, Zugangsdaten u. a.). Läuft als zusätzliche App
**auf Frappe Helpdesk** – Support-Tickets & Live-Chat kommen vom Helpdesk selbst.

Spezifikation/Vorlage: das frühere Next.js-Portal `CCconsulting-gmbh/cc-kundenportal`.

## Installation (auf bestehendem Frappe/Helpdesk-Bench)

```bash
# App ins Image backen (apps.json) ODER lokal holen:
bench get-app https://github.com/CCconsulting-gmbh/cc-portal-app
bench --site <site> install-app cc_portal
bench --site <site> migrate
```

## Hinweis Sicherheit
Dieser App-Code enthält **keine Geheimnisse** (keine API-Keys, keine Kundendaten). Secrets liegen
ausschließlich in der Frappe-Site-Konfiguration / in DocTypes – niemals im Repo.

## Module
- **CC Portal** – Projekte & Briefing-Workflow (Start), danach Rechnungen+Bitrix24, Loyalty,
  Buchung, Dokumente/Signatur, Zugangsdaten, Wissen, Stripe.

## Lizenz
MIT
