// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
Vue.config.productionTip = false


import $ from 'jquery'
// Vuex 的使用
import Vuex from 'vuex'
Vue.use(Vuex);
// 创建　Store
const store = new Vuex.Store({
  // 状态和每个组件的数据属性有关联
  state: { 
    allList:[],
    note:{
      title:'',
      content:'',
      markdown:'',
    }
  },
  mutations: {
    getAllDatas(state){

      $.ajax({
        url:'http://127.0.0.1:8000/api/v1/vue/',
        methods:'get',
        success:function(data){
          // console.log(data)
          // 拿不到， this 变了
          // console.log(this.$store)
          
          // 此处一定记得将数据从　JSON　格式反序列化
          data = JSON.parse(data)
  
          state.allList = data;
          // _this.$store.state.allList = data;
          // console.log(_this.$store.state.allList)
  
        }
      })
    },
    addOneNote(state, json){


      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/vue/",
        data: json,
        method:'post',
        success:function(data){
            console.log(data)

            _this.$store.state.allList = data
        },
        error:function(err){
            console.log(err)
        },
    })
    }
  },
  // actions: {
  //   addOneNote(context){
  //     context.commit('addOneNote')
  //   }
  // }
  })


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
