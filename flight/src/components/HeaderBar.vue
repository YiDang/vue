<template>
  <div class="header-bar">
    <el-row>
      <el-col v-if='!isManager' :span="3" :offset="3">
        <el-menu  :router="true" class="el-menu-demo" mode="horizontal" >
          <el-menu-item index="/main/book">Book</el-menu-item>
        </el-menu> 
      </el-col>
      <el-col :span="3" :offset="15">
        <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">
            <i class="el-icon-arrow-down el-icon--right">
              {{name}}
            </i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item v-if='!isManager' command="user">user</el-dropdown-item>
            <el-dropdown-item v-if='!isManager' command="record">record</el-dropdown-item>
            <el-dropdown-item command="logout">lougout</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-row>

  </div>
</template>

<script>
  import store from 'store'
  export default {
    name: 'header-bar',
    data () {
      return {
        name:'user9527',
        isManager:'',
      }
    },
    methods: {
      logout: function () {
        store.remove('token')
        this.$router.push({name: 'LoginView'})

      },
      handleCommand(command) {
        switch(command)
        {
          case 'logout':
          this.logout()
          break;
          case 'user':
          this.$router.push({name: 'UserInfoView'})
          break;
          case 'record':
          this.$router.push({name: 'RecordView'})
          break;
        }
      }
    },
    created: function created() {
      this.isHidden =false

      this.isManager = store.get('isManager')

      console.log('isManager',this.isManager)
    }
  }
</script>
<style type="text/css">
  .router-link-active{
    text-decoration: none;
  }
</style>