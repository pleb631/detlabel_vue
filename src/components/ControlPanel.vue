<template>
    <div class="control_panel">
        <slot></slot> <!-- 使用 slot 来接收内容 -->
    </div>
</template>

<script setup lang="ts" name="ControlPanel">

</script>

<style scoped>
.control_panel {
    background-color: yellow;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    flex-shrink: 0;
    width: 250px;
}
</style>
