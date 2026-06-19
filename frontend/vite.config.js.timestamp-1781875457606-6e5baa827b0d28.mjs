// vite.config.js
import path from "path";
import { defineConfig } from "file:///C:/Users/smeis/Downloads/cc-portal-app/frontend/node_modules/vite/dist/node/index.js";
import vue from "file:///C:/Users/smeis/Downloads/cc-portal-app/frontend/node_modules/@vitejs/plugin-vue/dist/index.mjs";
import frappeui from "file:///C:/Users/smeis/Downloads/cc-portal-app/frontend/node_modules/frappe-ui/vite/index.js";
var __vite_injected_original_dirname = "C:\\Users\\smeis\\Downloads\\cc-portal-app\\frontend";
var vite_config_default = defineConfig({
  plugins: [
    frappeui({
      frappeProxy: true,
      lucideIcons: true,
      jinjaBootData: true,
      buildConfig: {
        outDir: "../cc_portal/public/frontend",
        emptyOutDir: true,
        indexHtmlPath: "../cc_portal/www/cc_portal/index.html"
      }
    }),
    vue()
  ],
  resolve: {
    alias: {
      "@": path.resolve(__vite_injected_original_dirname, "src"),
      "tailwind.config.js": path.resolve(__vite_injected_original_dirname, "tailwind.config.js")
    }
  },
  optimizeDeps: {
    include: ["feather-icons", "tailwind.config.js"],
    exclude: ["frappe-ui"]
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCJDOlxcXFxVc2Vyc1xcXFxzbWVpc1xcXFxEb3dubG9hZHNcXFxcY2MtcG9ydGFsLWFwcFxcXFxmcm9udGVuZFwiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9maWxlbmFtZSA9IFwiQzpcXFxcVXNlcnNcXFxcc21laXNcXFxcRG93bmxvYWRzXFxcXGNjLXBvcnRhbC1hcHBcXFxcZnJvbnRlbmRcXFxcdml0ZS5jb25maWcuanNcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfaW1wb3J0X21ldGFfdXJsID0gXCJmaWxlOi8vL0M6L1VzZXJzL3NtZWlzL0Rvd25sb2Fkcy9jYy1wb3J0YWwtYXBwL2Zyb250ZW5kL3ZpdGUuY29uZmlnLmpzXCI7aW1wb3J0IHBhdGggZnJvbSBcInBhdGhcIjtcbmltcG9ydCB7IGRlZmluZUNvbmZpZyB9IGZyb20gXCJ2aXRlXCI7XG5pbXBvcnQgdnVlIGZyb20gXCJAdml0ZWpzL3BsdWdpbi12dWVcIjtcbmltcG9ydCBmcmFwcGV1aSBmcm9tIFwiZnJhcHBlLXVpL3ZpdGVcIjtcblxuZXhwb3J0IGRlZmF1bHQgZGVmaW5lQ29uZmlnKHtcbiAgcGx1Z2luczogW1xuICAgIGZyYXBwZXVpKHtcbiAgICAgIGZyYXBwZVByb3h5OiB0cnVlLFxuICAgICAgbHVjaWRlSWNvbnM6IHRydWUsXG4gICAgICBqaW5qYUJvb3REYXRhOiB0cnVlLFxuICAgICAgYnVpbGRDb25maWc6IHtcbiAgICAgICAgb3V0RGlyOiBcIi4uL2NjX3BvcnRhbC9wdWJsaWMvZnJvbnRlbmRcIixcbiAgICAgICAgZW1wdHlPdXREaXI6IHRydWUsXG4gICAgICAgIGluZGV4SHRtbFBhdGg6IFwiLi4vY2NfcG9ydGFsL3d3dy9jY19wb3J0YWwvaW5kZXguaHRtbFwiLFxuICAgICAgfSxcbiAgICB9KSxcbiAgICB2dWUoKSxcbiAgXSxcbiAgcmVzb2x2ZToge1xuICAgIGFsaWFzOiB7XG4gICAgICBcIkBcIjogcGF0aC5yZXNvbHZlKF9fZGlybmFtZSwgXCJzcmNcIiksXG4gICAgICBcInRhaWx3aW5kLmNvbmZpZy5qc1wiOiBwYXRoLnJlc29sdmUoX19kaXJuYW1lLCBcInRhaWx3aW5kLmNvbmZpZy5qc1wiKSxcbiAgICB9LFxuICB9LFxuICBvcHRpbWl6ZURlcHM6IHtcbiAgICBpbmNsdWRlOiBbXCJmZWF0aGVyLWljb25zXCIsIFwidGFpbHdpbmQuY29uZmlnLmpzXCJdLFxuICAgIGV4Y2x1ZGU6IFtcImZyYXBwZS11aVwiXSxcbiAgfSxcbn0pO1xuIl0sCiAgIm1hcHBpbmdzIjogIjtBQUEyVSxPQUFPLFVBQVU7QUFDNVYsU0FBUyxvQkFBb0I7QUFDN0IsT0FBTyxTQUFTO0FBQ2hCLE9BQU8sY0FBYztBQUhyQixJQUFNLG1DQUFtQztBQUt6QyxJQUFPLHNCQUFRLGFBQWE7QUFBQSxFQUMxQixTQUFTO0FBQUEsSUFDUCxTQUFTO0FBQUEsTUFDUCxhQUFhO0FBQUEsTUFDYixhQUFhO0FBQUEsTUFDYixlQUFlO0FBQUEsTUFDZixhQUFhO0FBQUEsUUFDWCxRQUFRO0FBQUEsUUFDUixhQUFhO0FBQUEsUUFDYixlQUFlO0FBQUEsTUFDakI7QUFBQSxJQUNGLENBQUM7QUFBQSxJQUNELElBQUk7QUFBQSxFQUNOO0FBQUEsRUFDQSxTQUFTO0FBQUEsSUFDUCxPQUFPO0FBQUEsTUFDTCxLQUFLLEtBQUssUUFBUSxrQ0FBVyxLQUFLO0FBQUEsTUFDbEMsc0JBQXNCLEtBQUssUUFBUSxrQ0FBVyxvQkFBb0I7QUFBQSxJQUNwRTtBQUFBLEVBQ0Y7QUFBQSxFQUNBLGNBQWM7QUFBQSxJQUNaLFNBQVMsQ0FBQyxpQkFBaUIsb0JBQW9CO0FBQUEsSUFDL0MsU0FBUyxDQUFDLFdBQVc7QUFBQSxFQUN2QjtBQUNGLENBQUM7IiwKICAibmFtZXMiOiBbXQp9Cg==
