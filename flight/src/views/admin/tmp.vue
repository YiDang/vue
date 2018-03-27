<template>
  <div id = "user-manage-view">
    <h1>User Management</h1>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'user-manage-view',
  // components: { HeaderBar },
  data () {
    return {

    }
  },
  methods: {
    onRegister:function(){
      console.log("register submit")
    },

  }
}
</script>