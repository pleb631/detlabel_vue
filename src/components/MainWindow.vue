<template>
    <div class="main_window">
        <img :src="img_data">
    </div>
    <!-- vue-konva -->
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import axios from 'axios';
import { useStore } from '@/stores/useStore';

const store = useStore();
const apiBaseUrl = store.apiBaseUrl;
let img_data = ref('');

// 监听 store.img_path 的变化，并根据新的路径获取图片
const stopWatch = watch(() => store.img_path, async (newValue, oldValue) => {
    const url = `${apiBaseUrl}/api/getImg/${encodeURIComponent(store.img_path_full)}`;
    try {
        // 使用 axios 发送 GET 请求
        const response = await axios.get(url);

        // 假设返回的数据结构是 { base64_data: '...' }
        img_data.value = response.data.base64_data;
    } catch (error) {
        console.error("请求失败", error);
    }
});
</script>


<style scoped>
.main_window {
    display: flex;
    background-color: rgb(23, 185, 255);
}
img {
  width: 100%;
  height: 100%;
  object-fit: contain;  /* 保持比例，适应容器 */
  object-position: center;  /* 确保图片居中对齐 */
}
</style>
