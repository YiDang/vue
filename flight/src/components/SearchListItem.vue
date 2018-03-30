<template>
  <div>
    <el-table
      border
      :data="travels"
      highlight-current-row
      @current-change="handleCurrentChange"
      style="width: 80%; margin: auto">
      <el-table-column
        prop="departure"
        label="from">
      </el-table-column>
      <el-table-column
        prop="arrival"
        label="to">
      </el-table-column>
      <el-table-column
        prop="date"
        label="date">
      </el-table-column>
      <el-table-column
        prop="duration"
        label="duration">
      </el-table-column>
      <el-table-column
        prop="stop_count"
        label="stops">
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
    </el-table>
  </div>
</template>

<script>

export default {
  name: 'search-list-item',
  props:['travels'],
  data(){
    return{
      currentRow:null,
    }
  },//1:go 2:back 0:generate result

  methods:{
    handleCurrentChange(val) {
      this.currentRow = val;
      this.$emit('rowChange',val);
    }
  }

}
</script>