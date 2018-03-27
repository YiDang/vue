<template>
  <div id = "active-flights-view">
  <h1>Most active flights</h1>
    <el-table
      :data="flights"
      style="width: 100%">
      <el-table-column
        prop="company"
        label="company"
        width="180">
      </el-table-column>
      <el-table-column
        prop="no"
        label="no"
        width="180">
      </el-table-column>
    </el-table>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'active-flights-view',
  // components: { HeaderBar },
  data () {
    return {
      flights:[{
        company:'UA',
        no:'350'
      }]
    }
  },
  methods: {
    onRegister:function(){
      console.log("register submit")
    },

  }
}
</script>