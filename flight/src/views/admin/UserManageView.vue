<template>
  <div id = "user-manage-view">
    <h1>User Management</h1>
    <el-row :gutter="10">
      <el-form :model="idForm" ref="idForm" label-width="100px">
      <el-col :span="8">
        <el-input prop="id" placeholder="id"></el-input>
      </el-col>
      <el-col :span="4">
        <el-button type = "submit" @click="onSearchSubmit">search</el-button>
      </el-col>
      </el-form>

      <el-col :span="4">
        <el-button @click="rVisible = true">register</el-button>
      </el-col>
    </el-row>
    
    <el-dialog
      title="Sign up"
      :visible.sync="rVisible"
      width="30%">
        <el-form ref="formr" :model="formr" >
          <el-form-item>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="id" placeholder="id" v-model="formr.id"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="password" placeholder="password" v-model="formr.password"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="rVisible = false">取 消</el-button>
          <el-button type="primary" @click="onRegister">确 定</el-button>
        </span>
      </el-dialog>

      <el-dialog
      title="Edit"
      :visible.sync="uVisible"
      width="40%">
        <el-form ref="formu" :model="formu" >
          <el-form-item>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input :disabled="true" name="id" placeholder="id" v-model="formu.id"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
          <el-form-item>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-input name="password" placeholder="password" v-model="formu.password"></el-input>
              </el-col>
            </el-row>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="uVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onSave">Save</el-button>
          <el-button type="danger" @click="onDelete">Delete</el-button>
        </span>
      </el-dialog>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

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
        id : '',
        password : ''        
      },
      formu:{
        id : '',
        password : ''        
      }
    }
  },
  methods: {
    onSearchSubmit:function(){
      console.log("search submit")
      this.uVisible = true
    },
    onRegister:function(){
      console.log("register submit")
    },
    onSave:function(){
      console.log("save submit")
    },
    onDelete:function(){
      console.log("delete submit")
    },
  }
}
</script>