<template>
	<div id = "record-view">
    <el-row :gutter=20>
      <el-checkbox-group v-model="checkList">
        <el-col :span="3" :offset="3">
          <el-checkbox label="current">current</el-checkbox>
        </el-col>
        <el-col :span="3">
          <el-checkbox label="history">history</el-checkbox>
        </el-col>
      </el-checkbox-group>
    </el-row>
		<record-list-item
    :hidden = 'existData'
		v-bind:travels="paged"
		></record-list-item>
    <el-pagination :hidden = 'existData' layout="prev, pager, 
    next" :total="listw84page.length" :page-size="pageSize" :current-page.sync="currentPage">
    </el-pagination>
    {{currentPage}}
	</div>
</template>



<script>

import RecordListItem from '../components/RecordListItem'
import { page } from '../components/page.js'
export default {
  name: 'record-view',

  components: {RecordListItem },

  mixins:[page],
  data () {
    return {
      checkList:[],
      // currentPage:1,
      // pageSize:5,
    	form:{
    		depart:'',
    		destination:'',
    		date1:'',
    		date2:'',
    	},
    	travels:[]
    }
  },
  computed: {
    existData: function () {
      // console.log(this.travels.length)
      return this.listw84page.length==0
    },
    listw84page:function(){
      var travels=[]
      var current=this.checkList.indexOf('current')>=0
      var history=this.checkList.indexOf('history')>=0
      this.travels.forEach(function(element) {
        var d = new Date(element.depart)
        var n = new Date()
        if((d>n && current)||(d<n && history))
          travels.push(element)
      });
      // console.log('filtered',travels.length)
      return travels
    }
    // paged:function(){
    //   var start = this.pageSize*(this.currentPage-1)
    //   var end = this.pageSize*this.currentPage
    //   var travels = []
    //   for(var i=start; i<end && i < this.filtered.length; i++){
    //     travels.push(this.filtered[i])
    //   }
    //   // console.log('paged',travels.length)
    //   return travels
    // }
  },
  methods: {
  },

  created: function created() {
    // console.log("created")
    this.travels = []
    // var Date1=new Date(2018, 0, 17, 3, 24, 0)
    var Date1=new Date("2018-01-17 3:24:0")
    var Date2=new Date(2018, 5, 17, 3, 24, 0)
  
    for(var i = 0; i < 10; i++){
      this.travels.push({
        id:i,
        from:'EWR',
        to:'JFK',
        depart: i<5 ? Date1.toString():Date2.toString(),
        // depart:Date1.toString(),
        arrive:'',
        price:100,
        history: true,
        current: true,
        stops:[
        {
          from:'a',
          to:'b',
          depart:'00:00',
          arrive:'00:00',
        },
        {
          from:'a',
          to:'b',
          depart:'00:00',
          arrive:'00:00',
        }
        ],
        passengers:[
          {
            name:'Bob',
          },
          {
            name:'Alice',
          }
        ]

      })
    }
  }
}
</script>