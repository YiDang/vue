<template>
  <div>
    <!-- {{travels}} -->
    <el-table
      border
      :data="travels"
      style="width: 100%">
      <el-table-column
        prop="id"
        label="id">
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
        prop="price"
        label="$price">
      </el-table-column>
      <el-table-column
        label='stops'>
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
    </el-table>
  </div>
</template>

<script>

export default {
  name: 'record-list-item',

  props:['travels'],

  methods:{
    test:function (){
      console.log(this.travels)
    }
  }

}
</script>