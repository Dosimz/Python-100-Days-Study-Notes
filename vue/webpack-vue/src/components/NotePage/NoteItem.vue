<template>
    <li>
        <h2>{{data.title}}</h2>
        <p>{{data.id}}</p>
    </li>
</template>

<script>
export default {
    name:'NoteItem',
    data(){
        return{

        }
    },
    props:{
        data:Object
    },
    computed:{}
}
</script>

<style scoped>

</style>

