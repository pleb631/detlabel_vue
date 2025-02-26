import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useStore = defineStore("use", () => {
  const apiBaseUrl = "http://127.0.0.1:5000";
  let img_path = ref("");
  let img_root = ref("");

  let img_path_full = computed(() => {
    return img_root.value +"\\"+ img_path.value;
  });
  return { apiBaseUrl, img_path, img_root, img_path_full};
});
