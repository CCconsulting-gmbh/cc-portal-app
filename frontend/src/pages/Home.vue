<template>
  <div class="mx-auto max-w-5xl px-6 py-10">
    <h1 class="text-2xl font-bold">Willkommen im CC Portal</h1>
    <p class="mt-1 text-ink-gray-6">
      Ihre Zentrale für Projekte, Rechnungen und mehr – im selben System wie das Helpdesk.
    </p>

    <div class="mt-6 rounded-xl border bg-surface-white p-5">
      <div class="text-sm text-ink-gray-6">Angemeldet als</div>
      <div class="mt-1 text-lg font-semibold">
        {{ user.data || "…" }}
      </div>
    </div>

    <div class="mt-6 grid grid-cols-2 gap-4 sm:grid-cols-4">
      <div
        v-for="m in modules"
        :key="m.label"
        class="rounded-xl border bg-surface-white p-4"
      >
        <div class="text-2xl">{{ m.icon }}</div>
        <div class="mt-2 font-medium">{{ m.label }}</div>
        <div class="text-xs text-ink-gray-5">{{ m.hint }}</div>
      </div>
    </div>

    <p class="mt-8 text-xs text-ink-gray-5">
      Dies ist das Grundgerüst. Als Nächstes kommen das echte Dashboard (KPIs + Diagramme)
      und die Modul-Seiten (Projekte, Briefing) im Helpdesk-Look.
    </p>
  </div>
</template>

<script setup>
import { createResource } from "frappe-ui";

const user = createResource({
  url: "frappe.auth.get_logged_user",
  auto: true,
});

const modules = [
  { icon: "◳", label: "Projekte", hint: "in Arbeit" },
  { icon: "€", label: "Rechnungen", hint: "geplant" },
  { icon: "★", label: "Loyalty", hint: "geplant" },
  { icon: "✉", label: "Tickets", hint: "aus Helpdesk" },
];
</script>
