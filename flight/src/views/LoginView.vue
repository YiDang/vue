<template>
  <div class="login-view">
      <el-form ref="form" :model="form" label-width="80px" @click.submit.prevent>
        <el-form-item>
          <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="4">
              <el-input name="id" placeholder="id" v-model="form.id"></el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item>
          <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="4">
              <el-input name="password" placeholder="password" v-model="form.password"></el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item>
          <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="4">
              <el-button @click="onSubmit">login</el-button>
            </el-col>
            <el-col :span="4">
              <el-button type = "submit" @click="openRegister">register</el-button>
            </el-col>
          </el-row>
        </el-form-item>
      </el-form>

      <el-form v-show= "isHidden" ref="form" :model="form" label-width="80px">
        <el-form-item>
          <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="4">
              <el-input name="id" placeholder="id" v-model="formr.id"></el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item>
          <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="4">
              <el-input name="password" placeholder="password" v-model="formr.password"></el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item>
          <el-row type="flex" class="row-bg" justify="center">
            <el-col :span="4">
              <el-button @click="onRegister">submit</el-button>
            </el-col>
          </el-row>
        </el-form-item>
      </el-form>
      <p>{{form.id}}</p>
      <p>{{form.password}}</p>
      <p>{{isHidden}}</p>
      <!-- <div class="">
        <button class="submit">submit
        </button>
      </div> -->
    <!-- </form> -->
  </div>
</template>

<script>
import store from 'store'
export default {
  name: 'login-view',
  data () {
    return {
      form : {
        id : '',
        password : ''
      },

      isHidden : false,

      formr:{
        id : '',
        password : ''        
      }
    }
  },
  methods: {
    created: function () {
      this.isHidden =false
      // console.log('here')
    },
    onSuccess: function (res) {
      this.$store.dispatch('login')
      // console.log('complete!')
      // this.$router.push({name: 'StatusView'})
    },
    onError: function (err) {
      // console.log(err)

    },
    onSubmit: function () {
      // this.$session.set('login', 'true')//
      // 登陆检测做到后端
      store.set('token','xxx')
      this.$router.push({name: 'MainView'})

      // Login...
      // this.$store.dispatch({
      //   type: 'login',
      //   email: this.email,
      //   token: this.token
      // }).then(res => {
      //   // Success handle
      //   this.onSuccess(res)
      // }, err => {
      //   // Error handle
      //   this.onError(err)
      // })
    },
    openRegister: function(){
      // console.log(this)
      // this.$store.dispatch('login') 
      // console.log("before",this.$store.state.login.loginState)
      // console.log(this.$session.exists('login'))
      this.isHidden = this.isHidden ? false:true 
    },
    onRegister: function(){
      
    }
  },
}
</script>

