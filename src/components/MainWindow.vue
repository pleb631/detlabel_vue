<template>
    <div class="main_window">
        <!-- {{ store.img_path }} -->
    </div>
</template>

<script setup lang="ts">

import { ref,watch } from 'vue';
import axios from 'axios';
import { useStore } from '@/stores/useStore';
const store = useStore();
const apiBaseUrl = store.apiBaseUrl;

const stopWatch = watch(()=>store.img_path, async (newValue, oldValue) => {
    const url = `${apiBaseUrl}/api/getImg/${store.img_root}/${encodeURIComponent(store.img_path)}`;
    try {
        const response = await fetch(url, {
            method: 'GET',
        });

        const data = await response.json();

    } catch (error) {
        console.error("请求失败", error);
    }
})

</script>

<style scoped>
.main_window {
    display: flex;
    background-color: rgb(23, 185, 255);
}
</style>
