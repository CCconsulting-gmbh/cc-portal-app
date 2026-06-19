import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import escape_html


class CCBriefing(Document):
	def after_insert(self):
		"""Kern-Workflow: Beim Anlegen eines Briefings automatisch ein Helpdesk-
		Übergabe-Ticket an die IT erstellen (best-effort – darf den Speichern-Vorgang
		nicht blockieren)."""
		self.create_handover_ticket()

	def create_handover_ticket(self):
		try:
			project = frappe.get_doc("CC Project", self.project)
			description = (
				"<b>Übergabe-Briefing (Vertrieb → IT)</b><br><br>"
				f"<b>Ziel:</b><br>{escape_html(self.goal or '')}<br><br>"
				f"<b>Umfang:</b><br>{escape_html(self.scope or '')}<br><br>"
				f"<b>Budget:</b> {escape_html(self.budget or '–')}<br>"
				f"<b>Deadline:</b> {self.deadline or '–'}<br>"
				f"<b>Referenzen:</b><br>{escape_html(self.references or '–')}"
			)
			ticket = frappe.get_doc(
				{
					"doctype": "HD Ticket",
					"subject": f"Übergabe an IT: {project.project_name}",
					"description": description,
					"raised_by": frappe.session.user,
				}
			)
			if project.customer:
				ticket.customer = project.customer
			ticket.insert(ignore_permissions=True)

			# Verknüpfung am Projekt vermerken (optional, nur wenn Feld existiert)
			frappe.msgprint(
				_("Übergabe-Ticket {0} an die IT wurde erstellt.").format(ticket.name),
				alert=True,
				indicator="green",
			)
		except Exception:
			frappe.log_error(frappe.get_traceback(), "CC Portal: Handover-Ticket fehlgeschlagen")
