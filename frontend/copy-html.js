// Kopiert die gebaute index.html aus dem Asset-Ordner in den www-Seitenordner,
// damit Frappe sie als Website-Seite unter /cc-portal ausliefert (mit Jinja-Boot-Daten).
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname } from "node:path";

const src = "../cc_portal/public/frontend/index.html";
const dest = "../cc_portal/www/cc_portal/index.html";

mkdirSync(dirname(dest), { recursive: true });
copyFileSync(src, dest);
console.log(`copied ${src} -> ${dest}`);
