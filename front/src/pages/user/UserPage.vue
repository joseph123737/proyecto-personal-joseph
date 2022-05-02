<template>
  <h1>{{user}}</h1>
</template>

<script>
export default {
  data(){
    return{
      user:{},
    }
  },
  mounted(){
    this.loadData()
  },
  methods:{
    async loadData(){
        let response =  await fetch(`http://192.168.21.143:5000/api/users/users-stats/${this.$route.params.id}`)
        this.user =  await response.json()
    }
  },

}
</script>

<style>

</style>