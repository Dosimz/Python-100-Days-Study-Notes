<template>
  <div id="app">
    <TabHeader/>
    <div style="text-align:center;">
    <img src="./assets/logo.png">
    </div>
    <router-view/>
  </div>
</template>
console.log(this.$store)
<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import TabHeader from './components/TabHeader'

import $ from 'jquery'
export default {
  name: 'App',
  components:{
    TabHeader
  },
  created(){
    
    },
  // 页面加载完成的方法
  mounted(){
    // var _this = this

    // $.ajax({
    //   url:'http://127.0.0.1:8000/api/v1/vue/',
    //   methods:'get',
    //   success:function(data){
    //     // console.log(data)
    //     // 拿不到， this 变了
    //     // console.log(this.$store)
        
    //     // 此处一定记得将数据从　JSON　格式反序列化
    //     data = JSON.parse(data)

    //     _this.$store.state.allList = data;
    //     // console.log(_this.$store.state.allList)

    //   }
    // })

    this.$store.commit('getAllDatas')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
