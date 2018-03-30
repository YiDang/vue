<template>
  <div class="admin-menu">
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">open</el-radio-button>
      <el-radio-button :label="true">close</el-radio-button>
    </el-radio-group>
    <el-menu :router="true" default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span slot="title">admin</span>
        </template>
        <el-menu-item-group>
          <span slot="title">Manager</span>
          <el-menu-item index="/usermanage">Customer Management</el-menu-item>
          <el-menu-item index="/salesreport">Sales Report</el-menu-item>
          <el-menu-item index="/allflights">All Flights</el-menu-item>
          <el-menu-item index="/reservation">Reservations</el-menu-item>
          <el-menu-item index="/revenue">Revenue</el-menu-item>
          <el-menu-item index="/activeflights">Active Flights</el-menu-item>
          <el-menu-item index="/seatreserve">Seats Reservation</el-menu-item>
          <el-menu-item index="/flightsofairport">Flights of Airport</el-menu-item>
          <el-menu-item index="/ontime">ETA</el-menu-item>
          <!-- <el-menu-item index="1-10">选项0</el-menu-item> -->
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
  export default {
    name: 'admin-menu',
    data () {
      return {
        isCollapse: true
      }
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    },
    created: function created() {

    }
  }
</script>