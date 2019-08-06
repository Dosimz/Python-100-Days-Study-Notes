<template>
  <div id="app">
    <TabHeader/>
    <div style="text-align:center;">
    <img src="./assets/logo.png">
    </div>
    <router-view/>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import TabHeader from './components/TabHeader'
export default {
  name: 'App',
  components:{
    TabHeader
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
