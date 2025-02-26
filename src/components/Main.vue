<script setup lang="ts" name="App">
import ControlPanel from "@/components/ControlPanel.vue";
import InfoPanel from "@/components/InfoPanel.vue";
import MainWindow from "@/components/MainWindow.vue";
</script>

<template>
    <div class="container">
        <ControlPanel class="control_panel">
        </ControlPanel>

        <MainWindow class="main_window"></MainWindow>
        <InfoPanel class="info_panel"></InfoPanel>
    </div>
</template>

<style scoped>
.container {
    width: 100vw;
    height: 100vh;
    border: 1px solid #000;
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-content: center;
    justify-content: flex-start;
    align-items: stretch;
}
.control_panel {
    width: 150px;
    height: 100vh;
}
.info_panel {
    
    box-sizing: border-box;
    width: 200px;
    height: 100vh;
    /* flex-grow:0.3; */
}

.main_window {
    flex-grow:1;
    height: 100vh;
}


</style>
