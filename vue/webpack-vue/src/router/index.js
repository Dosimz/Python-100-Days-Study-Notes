import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import MainPage from "@/components/MainPage/MainPage";
import NotePage from "@/components/NotePage/NotePage";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage1',
      component: MainPage
    },
    {
      path: '/note',
      name: 'NotePage1',
      component: NotePage,
    }
  ]
})
