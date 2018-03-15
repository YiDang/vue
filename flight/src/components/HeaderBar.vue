<template>
  <div class="header-bar">
    <h1 class="title">
      flight booking
    </h1>
    <!-- <el-button @click="logout">logout</el-button> -->
<!--     <div class="list-group">
      <router-link to="/book">Book</router-link>
      <router-link to="/user">UserInfo</router-link>
    </div> -->

    <el-menu :default-active="activeIndex" router='true' class="el-menu-demo" mode="horizontal" >
      <el-menu-item index="/main/book">Book</el-menu-item>
      <el-menu-item index="/main/user">UserInfo</el-menu-item>
      <el-menu-item index="/login">logout</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'header-bar',
  data () {
    return {}
  },
  methods: {
    logout: function () {
      // this.$session.remove('login')
      this.$router.push({name: 'LoginView'})
      // this.$router.push({ path: 'login' })
    },
  }
}
</script>