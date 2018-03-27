<template>
  <div id = "all-flights-view">
    <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.name" placeholder='name'></el-input>
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
      :data="flights"
      style="width: 100%">
      <el-table-column
        prop="company"
        label="company"
        width="180">
      </el-table-column>
      <el-table-column
        prop="stat1"
        label="stat1"
        width="180">
      </el-table-column>
    </el-table>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'all-flights-view',
  // components: { HeaderBar },
  data () {
    return {
      form:{
        company:''
      },

      flights:[{
        company:'UA',
        stat1:'1'
      }]
    }
  },
  methods: {
    onSearch:function(){
      console.log("search submit")
    },

  }
}
</script>