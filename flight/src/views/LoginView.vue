<template>
  <div class="login-view">
    <!-- <form method="get" @submit.prevent="onSubmit()"> -->
      <!-- <p v-if="error" class="tip error">{{error}}</p> -->
<!--       <div class="form-user">
        <label>
          <strong>邮箱</strong>
          <input
            v-model="id"
            name="id"
            placeholder="id">
        </label>
      </div>
      <div class="form-pwd">
        <label>
          <strong>密码</strong>
            <input
            v-model="password"
            name="password"
            placeholder="password">
        </label>
      </div> -->
      <el-form ref="form" :model="form" label-width="80px">
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
          </el-row>
        </el-form-item>
      </el-form>
      <p>{{form.id}}</p>
      <p>{{form.password}}</p>
      <!-- <div class="">
        <button class="submit">submit
        </button>
      </div> -->
    <!-- </form> -->
  </div>
</template>

<script>
export default {
  name: 'loginView',
  data () {
    return {
      form : {
        id : '',
        password : ''
      }
    }
  },
  methods: {

    onSuccess: function (res) {
      // console.log('complete!')
      this.$router.push({name: 'StatusView'})
    },
    onError: function (err) {
      // console.log(err)
      this.error = err.body.error
      this.loginState = '登录'
      this.isDisabled = false
    },
    onSubmit: function () {
      this.$router.push({name: 'BookView'})
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
    }
  },
}
</script>

