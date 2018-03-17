<template>
	<div id = "record-view">
		<record-list-item
    :hidden = 'existData'
		v-bind:travels="travels"
		></record-list-item>
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
        depart:'00:00',
        arrive:'00:00',
        price:100,
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
        ]

      })
    }
  }
}
</script>