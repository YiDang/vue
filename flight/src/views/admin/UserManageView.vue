<template>
  <div id = "user-manage-view">
    <h1>User Management</h1>
    <el-row :gutter="10">
      <el-form :model="idForm" ref="idForm" label-width="100px">
      <el-col :span="8">
        <el-input v-model='idForm.id' placeholder="id"></el-input>
      </el-col>
      <el-col :span="4">
        <el-button type = "submit" @click="onSearchSubmit">search</el-button>
      </el-col>
      </el-form>

      <el-col :span="4">
        <el-button @click="rVisible = true">register</el-button>
      </el-col>
    </el-row>
    {{searchres}}
    <el-dialog
      title="Sign up"
      :visible.sync="rVisible"
      width="30%">
        <el-form ref="formr" :model="formr" >
          <el-form-item label='account id:'>
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
        <span slot="footer" class="dialog-footer">
          <el-button @click="rVisible = false">取 消</el-button>
          <el-button type="primary" @click="onRegister">确 定</el-button>
        </span>
        {{rMessage}}
      </el-dialog>

      <el-dialog
      title="Edit"
      :visible.sync="uVisible"
      width="40%">
        <el-form ref="formu" :model="formu" >
          <el-form-item label='account id:'>
            <el-input name="id" placeholder="id" v-model="formu.id" :disabled='true'></el-input>
          </el-form-item>
          <el-form-item label='password:'>
            <el-input name="password" placeholder="password" v-model="formu.password"></el-input>
          </el-form-item>
          <el-form-item label='lastName:'>
            <el-input name="lastName" placeholder="lastName" v-model="formu.lastName"></el-input>
          </el-form-item>
          <el-form-item label='firstName:'>
            <el-input name="firstName" placeholder="firstName" v-model="formu.firstName"></el-input>
          </el-form-item>
          <el-form-item label='zipCode:'>
            <el-input name="zipCode" placeholder="zipCode" v-model="formu.zipCode"></el-input>
          </el-form-item>
          <el-form-item label='email:'>
            <el-input name="email" placeholder="email" v-model="formu.email"></el-input>
          </el-form-item>
          <el-form-item label='address:'>
            <el-input name="address" placeholder="address" v-model="formu.address"></el-input>
          </el-form-item>
          <el-form-item label='telephone:'>
            <el-input name="telephone" placeholder="telephone" v-model="formu.telephone"></el-input>
          </el-form-item>
          <el-form-item label='credit:'>
            <el-input name="credit" placeholder="credit" v-model="formu.credit"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="uVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onSave">Save</el-button>
          <el-button type="danger" @click="onDelete">Delete</el-button>
        </span>
        {{editres}}
      </el-dialog>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'
import {prefix} from '../../components/prefix'
export default {

  name: 'user-manage-view',
  // components: { HeaderBar },
  data () {
    return {
      rVisible:false,
      uVisible:false,
      idForm:{
        id:''
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
      formu:{
        id : '',
        password : ''        
      },
      searchres:'',
      editres:'',
      rMessage:''
    }
  },
  methods: {
    onSearchSubmit:function(){
      console.log("search submit")
      var params = new URLSearchParams();
      console.log(this.idForm.id)
      params.append('id', this.idForm.id);
      this.$axios({
        method: 'post',
        url:  prefix + '/api/showuser',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        console.log(response.data.error)
        if(response.data.error != undefined){
          this.searchres = 'id does not exist'
        }
        else{
          this.uVisible = true
          this.formu = response.data
        }
      })
    },
    onRegister:function(){
      console.log("register submit")
    },
    onSave:function(){
      console.log("save submit")
      var params = new URLSearchParams(this.formu);
      this.$axios({
        method: 'post',
        url:  prefix + '/api/edituser',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data.isedituser)
        this.editres=response.data.isedituser
        if(response.data.isedituser == 'Success')
          this.uVisible = false
      })
    },
    onDelete:function(){
      console.log("save submit")
      var params = new URLSearchParams(this.formu);
      this.$axios({
        method: 'post',
        url:  prefix + '/api/delete',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        // console.log(response.data)
        this.uVisible = false
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
          console.log('success')
          this.rVisible = false    
        }
        else{
          console.log('fail')
          this.rMessage='Account already exists!'
        }
      })
    },
  }
}
</script>