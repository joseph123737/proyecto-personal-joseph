<template>
  <h1>HAS ACERTADO: {{countOfGuest}} DE {{countOfMiss+countOfGuest}}</h1>
    <button @click="userDetail">ver perfil</button>
</template>

<script>
import {config} from '@/config.js'
export default {
  data(){
    return{
     countOfGuest :  parseInt(this.$route.params.guest),
     countOfMiss:parseInt(this.$route.params.miss),
     newData: {quizz_guest:parseInt(this.$route.params.guest),quizz_miss:parseInt(this.$route.params.miss)}
    }
  },
 methods:{
    async userDetail(){
        const userJson = localStorage.getItem("auth");
        const user = JSON.parse(userJson);
        const settings = {
              method: "PUT",
              body: JSON.stringify(this.newData),
              headers: {
                "Content-Type": "application/json"
              },
        };
        let response =  await fetch(`${config.API_PATH}/users/users-stats/change-stats/${user.user_id}`,settings)
        if (response.status == 200){
          this.$router.push({name:"user",params:{id:user.user_id}})
        }
    },
  },



}

</script>

<style>

</style>