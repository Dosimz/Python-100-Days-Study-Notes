<template>
<div>
    <ul>
        <NoteItem v-for = '(item, index) in getAllDatas' :key='index' :data='item'></NoteItem>
        <p>{{getAllDatas}}</p>
        <p>{{arra}}</p> 
    </ul>
    <!-- <p>{{getAllDatas}}</p> -->
</div>
</template>

<script>
import NoteItem from './NoteItem'
export default {
    name: 'NoteList',
    data(){
        console.log(this.$store)
        return {

        }
    },
    components:{
        NoteItem
    },
    computed:{
        arra(){
            return [{"id": 1, "title": "医生"}, {"id": 2, "title": "教师"}, {"id": 3, "title": "学生"}]
        },
        getAllDatas(){
            // var a = this.$store.state.allList
            // return JSON.parse(a);
            return this.$store.state.allList
        }
    },
}
</script>

<style scoped>

</style>

