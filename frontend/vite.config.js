import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import Icons from "unplugin-icons/vite";

// Wir nutzen NICHT das frappe-ui/vite-Plugin (das will sich beim Bauen mit einem
// Frappe-Server verbinden und hängt ohne Bench). Build-Ausgabe + Basis-Pfad setzen
// wir selbst; die index.html kopiert copy-html.js nach www/. Die frappe-ui-Komponenten
// funktionieren als normale Vue-Komponenten ohne das Plugin.
export default defineConfig({
  base: "/assets/cc_portal/frontend/",
  plugins: [vue(), Icons({ compiler: "vue3", autoInstall: false })],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
      // frappe-ui gibt src/style.css nicht via package "exports" frei -> direkt auf die Datei zeigen
      "frappe-ui/src/style.css": path.resolve(
        __dirname,
        "node_modules/frappe-ui/src/style.css"
      ),
    },
  },
  build: {
    outDir: "../cc_portal/public/frontend",
    emptyOutDir: true,
    target: "es2018",
  },
  optimizeDeps: {
    exclude: ["frappe-ui"],
  },
});
