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

      
      <!-- <el-button type="text" @click="dialogVisible = true">点击打开 Dialog</el-button> -->

      <el-dialog
      title="Sign up"
      :visible.sync="dialogVisible"
      width="30%"
      :before-close="handleClose">
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
<!--           <el-form-item>
            <el-row type="flex" class="row-bg" justify="center">
              <el-col :span="18">
                <el-button @click="onRegister">submit</el-button>
              </el-col>
            </el-row>
          </el-form-item> -->
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="onRegister">确 定</el-button>
        </span>
      </el-dialog>

      <el-button @click="onTest">submit</el-button>
      <p>{{form.id}}</p>
      <p>{{form.password}}</p>
      <!-- <div class="">
        <button class="submit">submit
        </button>
      </div> -->
    <!-- </form> -->
    </el-main>
  </div>
</template>

<script>
import store from 'store'
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
        id : '',
        password : ''        
      }
    }
  },
  methods: {
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
      if(this.form.id == '1') {
        console.log('Manager login')
        store.set('isManager',true) 
        this.$router.push({name: 'AdminView'})
      }
      else{
        console.log('Customer login')
        store.set('isManager',false)  
        this.$router.push({name: 'BookView'})
      } 
      
    },
    openRegister: function(){
      this.isHidden = this.isHidden ? false:true 
    },
    onRegister: function(){
      this.dialogVisible = false
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
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

