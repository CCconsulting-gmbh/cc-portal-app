<template>
  <div class="flex h-screen w-screen flex-col bg-surface-gray-1 text-ink-gray-9">
    <header class="flex h-14 shrink-0 items-center justify-between border-b bg-surface-white px-5">
      <div class="flex items-center gap-2">
        <div class="grid h-7 w-7 place-content-center rounded bg-surface-gray-7 text-sm font-bold text-ink-white">
          CC
        </div>
        <span class="text-base font-semibold">CC Portal</span>
      </div>
      <a
        href="/helpdesk"
        class="text-sm text-ink-gray-6 hover:text-ink-gray-9"
      >
        Zum Helpdesk →
      </a>
    </header>
    <main class="flex-1 overflow-auto">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
</script>
