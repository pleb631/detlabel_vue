<script setup lang="ts" name="App">
import ControlPanel from "@/components/ControlPanel.vue";
import InfoPanel from "@/components/InfoPanel.vue";
import MainWindow from "@/components/MainWindow.vue";
</script>

<template>
  <div class="container">
    <ControlPanel>
      sth1
      <!-- 可以在这里填充具体的内容 -->
    </ControlPanel>

    <MainWindow> sth2 </MainWindow>
    <InfoPanel>sth2</InfoPanel>
  </div>
</template>

<style scoped>
.container {
  width: 100vw;
  height: 100vh;
  border: 1px solid #000;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-content: center;
  justify-content: flex-start;
  align-items: stretch;
}
</style>
