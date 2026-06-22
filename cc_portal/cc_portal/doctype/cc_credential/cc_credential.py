from frappe.model.document import Document


class CCCredential(Document):
	"""Zugangsdaten-Tresor. Geheime Felder nutzen den Frappe-'Password'-Feldtyp:
	in der DB verschlüsselt (site-Key), in der UI maskiert. Export/Print/E-Mail
	sind in den Rechten bewusst deaktiviert, damit Geheimnisse nicht abfließen.

	Hinweis: Eine echte Ende-zu-Ende-Verschlüsselung (libsodium, Entschlüsselung
	nur im Browser) folgt in der Frontend-Phase – sie erfordert eine eigene UI.
	"""

	pass
