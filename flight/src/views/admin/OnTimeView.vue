<template>
  <div id = "on-time-view">
    <h1>User Management</h1>
    <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.flight" placeholder='flight'></el-input>
            </el-form-item>
          </el-col>
          <el-col :span=3>
            <el-form-item>
              <el-button type="submit" @click="onSearch">Search</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-row>
    <el-table
      v-show='show'
      :data="flights"
      style="width: 100%">
      <el-table-column
        prop="flight"
        label="flight"
        width="100">
      </el-table-column>
      <el-table-column
        prop="type"
        label="type"
        width="100">
      </el-table-column>
      <el-table-column
        prop="time"
        label="time"
        width="150">
      </el-table-column>
      <el-table-column
        prop="scheduletime"
        label="scheduletime"
        width="150">
      </el-table-column>
    </el-table>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'on-time-view',
  // components: { HeaderBar },
  data () {
    return {
     form:{
        airport:''
      },
      show:false,
      flights:[{
        flight:'ua350',
        type:'delayed',
        time:'',
        scheduletime:''
      },{
        flight:'ua350',
        type:'delayed',
        time:'',
        scheduletime:''
      }]
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      console.log("register submit")
    },

  }
}
</script>