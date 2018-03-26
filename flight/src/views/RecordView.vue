<template>
	<div id = "record-view">
    <el-row :gutter=20>
      <el-col :span="3" :offset="3">
        <el-checkbox v-model="current">current</el-checkbox>
      </el-col>
      <el-col :span="3">
        <el-checkbox v-model="history">history</el-checkbox>
      </el-col>
    </el-row>
		<record-list-item
    :hidden = 'existData'
		v-bind:travels="travels"
		></record-list-item>
    <el-pagination :hidden = 'existData' layout="prev, pager, next" :total="50" :page-size="10">
    </el-pagination>
	</div>
</template>



<script>

import RecordListItem from '../components/RecordListItem'

export default {
  name: 'record-view',

  components: {RecordListItem },

  data () {
    return {
    	form:{
    		depart:'',
    		destination:'',
    		date1:'',
    		date2:'',
    	},
    	travels:[

    	]
    }
  },
  computed: {
    existData: function () {
      // console.log(this.travels.length)
      return this.travels.length==0
    },
  },
  methods: {
  },

  created: function created() {
    // console.log("created")
    this.travels = []

    for(var i = 0; i < 10; i++){
      this.travels.push({
        id:i,
        from:'EWR',
        to:'JFK',
        depart:'2000-00-00 00:00',
        arrive:'2000-00-00 00:00',
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