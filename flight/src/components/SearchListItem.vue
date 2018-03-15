<template>
  <li class="search-list-item">  
  travel{{id}}:  
    {{from}},
    {{to}}
  </li>
</template>

<script>

export default {
  name: 'search-list-item',

  props:['id','from','to']

}
</script>