<script setup lang="ts">
import FilePanel from "@/components/FilePanel.vue";
</script>


<template>
    <div class="info_panel">

        <div class="label_panel">

        </div>
        <FilePanel class="file_panel"></FilePanel>
    </div>
</template>

<style scoped>
.info_panel {
    background-color: red;
    border-width: 10px;
    border-color: black;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    margin: auto;

    /* 添加样式 */
}

.label_panel {
    background-color: rgb(128, 230, 128);
    border-width: 1px;
    padding: 10px;
    border-color: black;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    flex-shrink: 0;
    width: 100%;
    height: 50%;
}


.file_panel {
    width: 100%;
    height: 50%;
    box-sizing: border-box;
}
</style>
