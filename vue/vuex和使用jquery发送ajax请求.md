## 1. Vuex

> - Vuex 是一个专为 Vue.js 应用程序开发的**状态管理模式**。它采用集中式存储管理应用的所有组件的状态.

  

####  code sample

创建设置 Vuex

```javascript
// main.js
// Vuex 的使用
import Vuex from 'vuex'
Vue.use(Vuex);
// 创建　Store
const store = new Vuex.Store({
  // 状态和每个组件的数据属性有关联
  state: { 
    allList:[]
  },
  mutations: {
  
  }
  })


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  // 这里加入 `store`
  store,
  components: { App },
  template: '<App/>'
})

```



## 2. 使用 jquery 发送 ajax 请求

从后端 api 接口获得数据并反序列化,然后存储在使用 Vuex 时设置的 allList 属性中。

```javascript
// App.vue

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
    var _this = this

    $.ajax({
      url:'http://127.0.0.1:8000/api/v1/roles/',
      methods:'get',
      success:function(data){
        // console.log(data)
        // 拿不到， this 变了
        // console.log(this.$store)

        // 此处一定记得将数据从　JSON　格式反序列化
        data = JSON.parse(data)
        
        _this.$store.state.allList = data;
        // console.log(_this.$store.state.allList)

      }
    })
  }
}
```



## 3. 展示获取的 Json 数据

先来到 NoteList.vue 组件文件中，这里是我们展现列表功能的组件。

> 如下图 List Note 区域

![](/run/media/yuyi/068AE93F8AE92BBD/python/vue/images/NoteList_00.png)

```html
<ul>
    <NoteItem v-for = '(item, index) in getAllDatas' :key='index' :data='item'></NoteItem>
    <p>{{getAllDatas}}</p>
    <p>{{arra}}</p> 
</ul>
```






```javascript
import NoteItem from './NoteItem'
export default {
    name: 'NoteList',
    data(){
        // console.log(this.$store)
        return {

        }
    },
    components:{
        NoteItem
    },
    
 	
    computed:{
        // 测试使用
        //arra(){
        //    return [{"id": 1, "title": "医生"}, {"id": 2, "title": "教师"}, {"id": 3, "title": "学生"}]
        //},
        // -------- 分割线 --------
        getAllDatas(){
            // var a = this.$store.state.allList
            // return JSON.parse(a);
            return this.$store.state.allList
        }
    },
}
```

## 传入数据到　NoteItem.vue　并展示具体内容

```vue
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
```

