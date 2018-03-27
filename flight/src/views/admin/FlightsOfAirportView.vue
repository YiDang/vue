<template>
  <div id = "flights-of-airport-view">
    <h1>Flight of given airport</h1>
    <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.airport" placeholder='airport'></el-input>
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
        prop="day"
        label="day"
        width="180">
      </el-table-column>
      <el-table-column
        prop="type"
        label="type"
        width="180">
      </el-table-column>
      <el-table-column
        prop="time"
        label="time"
        width="180">
      </el-table-column>
    </el-table>
    
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'flights-of-airport-view',
  // components: { HeaderBar },
  data () {
    return {
      form:{
        airport:''
      },
      show:false,
      flights:[{
        day:'Monday',
        time:'00:00',
        type:'arrive'
      },{
        day:'Monday',
        time:'00:00',
        type:'depart'
      }]
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      console.log("search submit")
    },

  }
}
</script>