<template>
  <h1>{{countOfGues_1}}</h1>
</template>

<script>
export default {
  data(){
    return{
     countOfGues_1 : this.$route.params.guest
    }
  },


}

</script>

<style>

</style>