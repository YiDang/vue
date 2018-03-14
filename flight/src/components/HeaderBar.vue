<template>
  <div class="header-bar">
    <h1 class="title">
    flight booking
    </h1>
    <div class="list-group">
          <!--使用指令v-link进行导航-->
          <!-- <a class="list-group-item" v-link="{ path: '/home'}">Home</a> -->
          <!-- <a class="list-group-item" v-link="{ path: '/about'}">About</a> -->
          <router-link to="/book">Book</router-link>
          <router-link to="/user">UserInfo</router-link>
        </div>
  </div>
</template>

<script>
export default {
  name: 'header-bar',
  data () {
    return {}
  },
  methods: {
  }
}
</script>