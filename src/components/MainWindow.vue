<template>
    <div class="main_window">
        <slot></slot> <!-- 使用 slot 来接收内容 -->
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
.main_window {
    display: flex;
    background-color: rgb(23, 185, 255);
    flex-grow:3;
    justify-content:center;
    align-items:center;  
}
</style>
