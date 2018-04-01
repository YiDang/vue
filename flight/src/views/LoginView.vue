<template>
  <div class="login-view">
  <el-header/>
  <el-main>
      <el-form ref="form" :model="form" label-width="0px" @click.submit.prevent>
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
              <el-button type = "submit" @click="dialogVisible = true">register</el-button>
            </el-col>
          </el-row>
        </el-form-item>
      </el-form>
      <el-dialog
      title="Sign up"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose">
        <el-form ref="formr" :model="formr" >
          <el-form-item label='Username:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="id" placeholder="id" v-model="formr.id" ></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='password:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="password" placeholder="password" v-model="formr.password"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='lastName:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="lastName" placeholder="lastName" v-model="formr.lastName"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='firstName:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="firstName" placeholder="firstName" v-model="formr.firstName"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='zipCode:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="zipCode" placeholder="zipCode" v-model="formr.zipCode"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='email:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="email" placeholder="email" v-model="formr.email"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='address:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="address" placeholder="address" v-model="formr.address"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='telephone:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="telephone" placeholder="telephone" v-model="formr.telephone"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item label='credit:'>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="credit" placeholder="credit" v-model="formr.credit"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
        </el-form>
        {{this.rMessage}}
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onRegister">Register</el-button>
        </span>
      </el-dialog>
      {{sMessage}}
    </el-main>
  </div>
</template>

<script>
import store from 'store'
import {prefix} from '../components/prefix'
export default {
  name: 'login-view',
  data () {
    return {
      dialogVisible: false,
      form : {
        id : '',
        password : ''
      },

      formr:{
        id : '1',
        password : '1',
        lastName:'1',
        firstName:'1',
        zipCode:'1',
        address:'1',
        email:'1',
        telephone:'1',
        credit:'1'
      },
      rMessage:'',
      sMessage:''
    }
  },
  methods: {
    onSuccess: function (res) {
      console.log('sucess!')
      store.set('token', res)
      if(res.isManager){
        console.log("manager")
        store.set('isManager',true)
        this.$router.push({name: 'AdminView'})
      }
      else{
        console.log("customer")
        store.set('isManager',false)
        this.$router.push({name: 'BookView'})
      }
    },
    onError: function (err) {
      // console.log(err)
      this.sMessage ='User does not exist or password is not correct'

    },

    onSubmit:function(){
      // onSuccess('')
      var params = new URLSearchParams();
      params.append('id', this.form.id);
      params.append('password', this.form.password);  
      this.$axios({
        method: 'post',
        url:  prefix + '/api/isUser',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        if(response.data.validUser){
          this.onSuccess(response.data)
        }
        else{
          this.onError(response.data)
        }
      })
    },

    onRegister: function(){

      var params = new URLSearchParams(this.formr);
      // params.append('id', this.form.id);
  
      this.$axios({
        method: 'post',
        url:  prefix + '/api/signUp',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        if(response.data.isSignUp){
          this.dialogVisible = false    
        }
        else{
          this.rMessage='Account already exists!'
        }
      })
    },
    handleClose(done) {
      this.$confirm('close？')
      .then(_ => {
        done();
      })
      .catch(_ => {});
    },
    onTest:function(){
      this.$axios({
        method: 'post',
        url:  '/api/',
        data: 'data'
      }).then(response => {
        console.log(response.data)
        console.log(response.status)
        console.log(response.statusText)
        console.log(response.headers)
        console.log(response.config)
      })
    }
  },
}
</script>

