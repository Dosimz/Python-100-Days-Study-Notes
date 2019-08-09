<template>
    <div class="container">
        <div class="row">
            <div class="col-md-3">
                <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">List Note</h3>
                </div>
                <div class="panel-body">
                <!-- 笔记列表 -->
                    <NoteShow/>
                </div>
                </div>
            </div>

            <div class="col-md-9">
                <!-- markdown　编辑器 -->
                <div class="panel panel-info">
                <div class="panel-heading">

                </div>
                <div class="panel-body">
                    <NoteMark/>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NoteMark from './NoteMark'
import NoteShow from './NoteShow'

export default {
    name:'NotePage',
    data(){
        return{

        }
    },
    components:{
        NoteMark,
        NoteShow

    }
}
</script>

<style scoped>

</style>

