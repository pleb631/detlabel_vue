<template>
    <div class="files_panel">
        <form @submit="submitForm">
            <input type="text" v-model="fileName" />
            <button type="submit">查找</button>
        </form>

        <div class="file_list">
            <input type="label" @click="click_fileitem($event)" class="fileitem" v-for="file in file_list" :key="file" :value="file">
        </div>
    </div>
</template>



<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import { useStore } from '@/stores/useStore';
let fileName = ref('');
let file_list = ref([]);
const store = useStore();
const apiBaseUrl = store.apiBaseUrl;
const submitForm = async (event: Event) => {
    event.preventDefault();
    if (!fileName.value) {
        alert("请输入文件名！");
        return;
    }

    // 构建动态 URL
    const url = `${apiBaseUrl}/api/getFiles/${encodeURIComponent(fileName.value)}`;
    try {
        const response = await fetch(url, {
            method: 'GET',
        });

        const data = await response.json();
        handleFilechange(data)
    } catch (error) {
        console.error("请求失败", error);
    }
}


function handleFilechange(data: any) {
    file_list.value.splice(0, file_list.value.length);
    file_list.value = [];
    if (data["paths"].length==0){
        alert("未找到文件");
        return;
    }
    if (data["paths"].length==1){
        file_list.value.push(data["paths"][0]);
    }
    else{
        file_list.value = Array.from(data["paths"])
    }
    console.log(data["base_path"])
    store.$patch({
        img_path: '',
        img_root: data["base_path"]
    })
    

}


function click_fileitem(event: Event) {
    const target = event.target as HTMLInputElement;
    store.$patch({
        img_path: target.value,
    })

}
</script>


<style scoped>

.fileitem:hover {
    cursor: pointer;

}

.fileitem:focus {
    background-color: rgb(128, 230, 128);
}
.fileitem{
    /* flex-shrink: 0; */
    background-color: rgb(212, 199, 199);
    
    font-size: 1rem;
    padding: 10px;
    border-color: black;
    border-width: 1px;
    border-style: solid;
    width: auto;
    overflow: visible;
    white-space: nowrap;

}
.file_list {
    background-color: rgb(128, 230, 128);
    border-width: 1px;
    overflow: auto;
    border-color: black;
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    flex-grow:1;
    align-items:baseline;
    
}
.files_panel {
    background-color: rgb(180, 222, 31);
    border-width: 10px;
    padding: 10px;
    border-color: black;
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    flex-shrink: 0;
}
</style>