## Vue 路由

第一步当然是来到我们 router 路由文件下面的 index.js，可以看出在这里我们用

- `path` 表示路径
- `component` 绑定对应组件
- `name` 用来命名。  

![](/run/media/yuyi/068AE93F8AE92BBD/python/vue/images/router_00.png)





首页组件的代码　MainPage.vue
```javascript
<template>
    <div class="main">
        首页
    </div>
</template>

<script>
export default {
    name:'MainPage',
    data(){
        return{

        }
    }
}
</script>
<style scoped>

</style>
```






笔记组件的代码　NotePage.vue
```javascript
<template>
    <div class="note">
        笔记
    </div>
</template>

<script>
export default {
    name:'NotePage',
    data(){
        return{

        }
    }
}
</script>

<style scoped>

</style>


```





## 导航栏　Tab



首先是创建一个导航栏的组件 TabHeader.vue
这里面我们直接引入 bootstrat 的示例导航栏，在此基础上对 `li` 标签做一定修改。


![](/run/media/yuyi/068AE93F8AE92BBD/python/vue/images/router_01.png)





- 创建可供循环的 `li` 标签资源　![](/run/media/yuyi/068AE93F8AE92BBD/python/vue/images/Tab_00.png)



- `v-for='(item, index) in routes' :key='item'` 遍历 `li` 标签

- 绑定 `class` 属性，用 `{active:index==currentIndex}` 判断 `li` 标签是否处于激活态

- `@click='activeHandler(index)'` 创建 click 事件，绑定 `activeHandler` 方法并传入 `index`  
```javascript
......
    methods: {
            activeHandler(index){
                this.currentIndex = index
            }
        },
......
```

  

### yarn run dev

![](/run/media/yuyi/068AE93F8AE92BBD/python/vue/images/result_00.png)

![](/run/media/yuyi/068AE93F8AE92BBD/python/vue/images/result_01.png)