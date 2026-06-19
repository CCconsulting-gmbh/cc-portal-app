import frappe
from frappe import _
from frappe.model.document import Document


class CCProject(Document):
	def validate(self):
		self.enforce_development_gate()

	def enforce_development_gate(self):
		"""Geschäftsregel (hart kodiert): Status 'Entwicklung' ist nur erlaubt,
		wenn das verknüpfte Briefing als vollständig markiert ist."""
		if self.status != "Entwicklung":
			return

		completed = frappe.db.get_value("CC Briefing", {"project": self.name}, "completed")
		if not completed:
			frappe.throw(
				_(
					"Status <b>Entwicklung</b> ist erst möglich, wenn das Briefing zu diesem "
					"Projekt vollständig ausgefüllt und freigegeben ist "
					"(Häkchen <b>Vollständig</b> im Briefing setzen)."
				),
				title=_("Briefing noch nicht freigegeben"),
			)
