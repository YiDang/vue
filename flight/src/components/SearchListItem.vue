<template>
<!--   <li class="search-list-item">  
  travel{{id}}:  
    {{from}},
    {{to}},
    {{stops}}
    <button @click = 'test'/>
  </li> -->
  <div>
    <!-- {{travels}} -->
  <el-table
      border
      :data="travels"
      style="width: 100%">
      <el-table-column
        prop="id"
        label="id"
        width="180">
      </el-table-column>
      <el-table-column
        prop="from"
        label="from"
        width="180">
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
        label='stops'
        >
        <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <!-- {{scope.row.stops}} -->
          <el-table :data="scope.row.stops">
            <el-table-column width="150" property="from" label="from"></el-table-column>
            <el-table-column width="100" property="to" label="to"></el-table-column>
            <el-table-column width="300" property="depart" label="depart"></el-table-column>
            <el-table-column width="300" property="arrive" label="arrive"></el-table-column>
          </el-table>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">details</el-tag>
          </div>
        </el-popover>
        </template>    
    
      </el-table-column>

  </el-table>
</div>
</template>

<script>

export default {
  name: 'search-list-item',

  props:['travels'],

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
    }
  }

}
</script>