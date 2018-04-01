<template>
	<div id = "itineraryView-view">
    <el-table :data="stops" >
      <el-table-column property="airlineCode" label="airlineCode"></el-table-column>
      <el-table-column property="flight_no" label="flight_no"></el-table-column>
      <el-table-column property="departure_airport" label="departure_airport"></el-table-column>
      <el-table-column property="arrival_airport" label="arrival_airport"></el-table-column>
      <el-table-column property="date" label="date"></el-table-column>
      <el-table-column property="departure_time" label="departure_time"></el-table-column>
      <el-table-column property="arrival_time" label="arrival_time"></el-table-column>
      <el-table-column property="duration" label="duration"></el-table-column>
    </el-table>
    <el-table
      :data="row.passenger_info"
      style="width: 80%; margin: auto">
        <el-table-column
        prop="ssn"
        label="ssn"
        width="180">
        </el-table-column>
        <el-table-column
        prop="name"
        label="name"
        width="180">
        </el-table-column>
      </el-table>
	</div>
</template>



<script>
import {prefix} from '../components/prefix'
export default {
  name: 'itineraryView-view',

  components: {},

  data () {
    return {
      row:null
    }
  },
  computed: {
    stops:function(){
      return this.row.stops.go.concat(this.row.stops.back)
    }
  },
  methods: {

  },

  created: function() {
    this.row = this.$route.params
  }

}
</script>
