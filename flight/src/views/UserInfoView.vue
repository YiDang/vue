<template>
  <div id = "userinfo-view">
    <h1>User page</h1>
    <el-form ref="formu" :model="formu" >
      <el-form-item>
        <el-row type="flex" class="row-bg" justify="center">
        <el-col :span="10">
            <el-input :disabled="true" name="id" placeholder="id" v-model="formu.id"></el-input>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item>
        <el-row type="flex" class="row-bg" justify="center">
          <el-col :span="10">
            <el-input name="password" placeholder="password" v-model="formu.password"></el-input>
          </el-col>
        </el-row>
      </el-form-item>
      <el-button type="submit" @click="onSave">Save</el-button>
    </el-form>
  </div>
</template>



<script>
import HeaderBar from '../components/HeaderBar'

export default {

  name: 'userinfo-view',
  components: { HeaderBar },
  data () {
    return {
      formu:{
        id : '',
        password : ''        
      }
    }
  },
  methods: {
    onSave:function(){
      console.log("save submit")
    },
  }
}
</script>