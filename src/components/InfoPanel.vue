<template>
    <div class="info_panel">
        <slot></slot> <!-- 使用 slot 来接收内容 -->
    </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.info_panel {
    background-color: red;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    flex-grow:1;
    /* 添加样式 */
}
</style>
