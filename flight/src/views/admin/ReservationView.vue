<template>
  <div id = "reservation-view">
    <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.input" :placeholder='form.ph'></el-input>
            </el-form-item>
          </el-col>
          <el-col :span=6>
            <el-select v-model="groupby" placeholder="search by">
              <el-option
              v-for="item in form.typeEnum"
              :key="item.label"
              :label="item.label"
              :value="item.label">
              </el-option>
            </el-select>
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
      :data="reservation"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="name"
        v-if="'name' == groupby"
        width="180">
      </el-table-column>
      <el-table-column
        prop="flight"
        label="flight"
        v-if="'flight' == groupby"
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

  name: 'reservation-view',
  // components: { HeaderBar },
  data () {
    return {
      form:{
        input:'',
        ph:'',
        flight:'',
        name:'',
        typeEnum:[{
          label:'name'
        },{
          label:'flight'
        }],
      },
      show:false,
      groupby:'',
      reservation:[]
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      console.log("register submit")
    },

  },
  watch:{
    groupby: function(){
        if(this.groupby=='name'){
            this.form.name = this.form.input
            this.form.ph = 'customer name'
            this.show = false
        }
        if(this.groupby=='flight'){
            this.form.flight = this.form.input
            this.form.ph = 'flight'
            this.show = false
        }
    }
  }
}
</script>