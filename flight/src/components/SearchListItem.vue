<template>
  <div>
    <el-table
      border
      :data="travels"
      style="width: 80%; margin: auto">
      <el-table-column
        label="id"
        prop="id"
        v-if="direction==0">
      </el-table-column>
      <el-table-column
        label="id"
        v-else>
        <template slot-scope="scope">
          <el-radio v-model="radio1" @change='onChange(scope.row)' :label="scope.row.id">
          </el-radio>
        </template>
      </el-table-column>

      <el-table-column
        prop="from"
        label="from">
      </el-table-column>
      <el-table-column
        prop="to"
        label="to">
      </el-table-column>
      <el-table-column
        prop="depart"
        label="depart">
      </el-table-column>
      <el-table-column
        prop="arrive"
        label="arrive">
      </el-table-column>
      <el-table-column
        label="stops">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <el-table :data="scope.row.stops">
              <el-table-column property="from" label="from"></el-table-column>
              <el-table-column property="to" label="to"></el-table-column>
              <el-table-column property="depart" label="depart"></el-table-column>
              <el-table-column property="arrive" label="arrive"></el-table-column>
            </el-table>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">details</el-tag>
            </div>
          </el-popover>
        </template>    
      </el-table-column>
      <el-table-column
        prop="price"
        label="$price">
      </el-table-column>
<!--       <el-table-column label="buy">
        <template slot-scope="scope">
          <el-button @click='buy(scope.row)'>buy
          </el-button>
          <el-radio v-model="radio1" :label="scope.row.id">
          </el-radio>
        </template>
      </el-table-column> -->
    </el-table>
  </div>
</template>

<script>

export default {
  name: 'search-list-item',
  data(){
    return{
      radio1:''
    }
  },
  props:['travels','direction'],//direction 1:go 2:back 3:generate result

  // date:{
  //   id:'',
  //   from:'',
  //   to:'',
  //   stops:[
  //   ]
  // },
  methods:{
    test:function (){
      console.log(this.travels)
    },
    buy:function (a){
      console.log(a)
    },
    onChange:function(data){
      // console.log(data)
      this.$emit('childEvent', {data:data,direction:this.direction})
    }
  }

}
</script>