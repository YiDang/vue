<template>
  <div>
    <el-table
      border
      :data="travels"
      style="width: 80%; margin: auto">
      <el-table-column
        prop="id"
        label="id">
      </el-table-column>
      <el-table-column
        prop="Departure"
        label="from">
      </el-table-column>
      <el-table-column
        prop="Arrival"
        label="to">
      </el-table-column>
      <el-table-column
        prop="RoundTrip"
        label="type">
      </el-table-column>
      <el-table-column
        label='stops'>
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
          <el-table :data="scope.row.stops.go" >
            <el-table-column property="airlineCode" label="airlineCode"></el-table-column>
            <el-table-column property="flight_no" label="flight_no"></el-table-column>
            <el-table-column property="departure_airport" label="departure_airport"></el-table-column>
            <el-table-column property="arrival_airport" label="arrival_airport"></el-table-column>
            <el-table-column property="date" label="date"></el-table-column>
            <el-table-column property="departure_time" label="departure_time"></el-table-column>
            <el-table-column property="arrival_time" label="arrival_time"></el-table-column>
            <el-table-column property="duration" label="duration"></el-table-column>
            <el-table-column property="booking_fee" label="booking_fee"></el-table-column>
            <el-table-column property="total_fare" label="total_fare"></el-table-column>
          </el-table>
          <el-table :data="scope.row.stops.back" v-show='scope.row.stops.back.length!=0'>
            <el-table-column property="airlineCode" label="airlineCode"></el-table-column>
            <el-table-column property="flight_no" label="flight_no"></el-table-column>
            <el-table-column property="departure_airport" label="departure_airport"></el-table-column>
            <el-table-column property="arrival_airport" label="arrival_airport"></el-table-column>
            <el-table-column property="date" label="date"></el-table-column>
            <el-table-column property="departure_time" label="departure_time"></el-table-column>
            <el-table-column property="arrival_time" label="arrival_time"></el-table-column>
            <el-table-column property="duration" label="duration"></el-table-column>
            <el-table-column property="booking_fee" label="booking_fee"></el-table-column>
            <el-table-column property="total_fare" label="total_fare"></el-table-column>
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
      <el-table-column
        label='passengers'>
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
          <el-table :data="scope.row.passenger_info">
            <el-table-column property="name" label="name" width='150px'></el-table-column>
            <el-table-column property="ssn" label="ssn" width='120px'></el-table-column>
          </el-table>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">details</el-tag>
          </div>
          </el-popover>
        </template>    
      </el-table-column>
      <el-table-column
        label="Itinerary">
        <template slot-scope="scope">
          <el-button @click="viewItinerary(scope.row)" type="text" size="small">view</el-button>
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
    },
    viewItinerary:function (row){
      // this.$router.push({path:"/main/itinerary",params:{a:1,b:2}})
      this.$router.push({name:'ItineraryView',params:row})
    }
  }

}
</script>