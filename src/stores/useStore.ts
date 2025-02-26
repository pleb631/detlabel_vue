import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useStore = defineStore("use", () => {
  const apiBaseUrl = "http://127.0.0.1:5000";

  return { apiBaseUrl };
});
