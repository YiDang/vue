<template>
  <div id = "userinfo-view">
    <h1>User page</h1>
    <el-form ref="formu" :model="formu" size='medium' label-width="120px" style="width: 70%;margin:0% 15%" >
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
      <el-button type="submit" @click="onSave">Save</el-button>
    </el-form>
    {{editres}}
  </div>
</template>



<script>
import HeaderBar from '../components/HeaderBar'
import store from 'store'

export default {

  name: 'userinfo-view',
  components: { HeaderBar },
  data () {
    return {
      formu:{
        no:'',
        id : '1',
        password : '1',
        lastName:'1',
        firstName:'1',
        zipCode:'1',
        address:'1',
        email:'1',
        telephone:'1',
        credit:'1',
        preference:''
      },
      editres:''
    }
  },
  methods: {
    onSave:function(){
      console.log("save submit")
      var params = new URLSearchParams(this.formu);
      this.$axios({
        method: 'post',
        url:  '/api/api/edituser',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data.isedituser)
        this.editres=response.data.isedituser
      })
    },
  },
  created: function() {
    var id =store.get('token').id
    console.log(id)
    var params = new URLSearchParams();
    params.append('id', id);
    this.$axios({
        method: 'post',
        url:  '/api/api/showuser',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        this.formu = response.data
      })
      // this.formu.id=
  }
}
</script>