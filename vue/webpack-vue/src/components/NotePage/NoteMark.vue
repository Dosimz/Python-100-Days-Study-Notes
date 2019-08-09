<template>
    
    <div class="wrap">
            请输入标题 <input type="text" name="" v-model="titleHandler">
        <button class="btn btn-success" @click='addOneNote'>提交</button>
        <div class="mark">
            <textarea class="editor" v-model='markdownHandler' cols="100" rows="10"></textarea>
            <div class="show" v-html="currentValue" ref="t"></div>
    
        </div>
    </div>  
</template>

<script>
import $ from 'jquery'
import Marked from 'marked'
export default {
    name:'NoteMark',
    data(){
        return {
            // markValue:'',

        }
    },
    methods:{
        addOneNote(){
            var json = {
                title:this.titleHandler,
                markdown: this.markdownHandler,
                content: this.$refs.t.innerText
            };
            // console.log(json)
            this.$store.commit('addOneNote', json);

// ------------ 分割线 ------------------
            // var _this = this

            // $.ajax({
            //     url: "http://127.0.0.1:8000/api/v1/vue/",
            //     data: json,
            //     method:'post',
            //     success:function(data){
            //         console.log(data)

            //         _this.$store.state.allList = data
            //     },
            //     error:function(err){
            //         console.log(err)
            //     },
            // })
        }
    },
    computed:{
        titleHandler:{
            set:function(newValue){
                // console.log('title'+newValue)
                this.$store.state.note.title = newValue
            },
            get:function(){
                return this.$store.state.note.title
            }
        },
        markdownHandler:{
            set:function(newValue){
                // console.log('markdown'+ newValue)
                this.$store.state.note.markdown = newValue;
            },
            get:function(){
                return this.$store.state.note.markdown;
            }
        },
        currentValue(){
            return Marked(this.markdownHandler);
        }
    }
}
</script>

<style scoped>
.t {
    width: 300px;
    height: 100px;
}
.mark{
    width: 800px;
    height: 400px;
    margin: 0 auto;
}

.editor,.show {
    float: left;
    width: 397px;
    height: 400px;
    border: 1px solid #666;
}
</style>
