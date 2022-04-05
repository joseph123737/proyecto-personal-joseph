<template>
  <h1>HAS ACERTADO: {{countOfGuest}} DE {{countOfMiss+countOfGuest}}</h1>
  <router-link :to="{name:'user'}">
    <button>ver perfil</button>
  </router-link>
</template>

<script>
export default {
  data(){
    return{
     countOfGuest :  parseInt(this.$route.params.guest),
     countOfMiss:parseInt(this.$route.params.miss),
     newData: {guest:this.countOfGuest,miss:this.countOfMiss}
    }
  },
  // methods:{
  //   updateUser(){
  //     const settings = {
  //       method: "PUT",
  //       body: JSON.stringify(this.newData),
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //     };
  //     await fetch('api/users/01', settings);
  //   }
  // },



}

</script>

<style>

</style>