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
        label="stops details">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <el-table :data="scope.row.stops">
              <el-table-column property="airlineCode" label="airlineCode"></el-table-column>
              <el-table-column property="flight_no" label="flight no"></el-table-column>
              <el-table-column property="departure_airport" label="from"></el-table-column>
              <el-table-column property="arrival_airport" label="to"></el-table-column>
              <el-table-column property="departure_time" label="departure time"></el-table-column>
              <el-table-column property="arrival_time" label="arrival time"></el-table-column>
              <el-table-column property="duration" label="duration" show-overflow-tooltip></el-table-column>
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