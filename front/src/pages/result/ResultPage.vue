<template>
  <main class="main">
    <h1>HAS ACERTADO: {{countOfGuest}} DE {{countOfMiss+countOfGuest}}</h1>
    <button @click="userDetail" class="btn-check-profile">ver perfil</button>


  </main>
</template>

<script>
import {updateUsersStats} from '@/services/api.js'
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
        let response =  await updateUsersStats(this.newData,)
        if (response.status == 200){
          this.$router.push({name:"user",params:{id:user.user_id}})
        }else{
          alert("algo a salido mal")
        }
    },
  },



}

</script>

<style scoped>
.main{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.btn-check-profile{
    background-color: #0c1bee;
    padding: 0.5em;
    border: 2px solid #0a16bd;
    border-radius:2em;
    color: white;
}

.btn-check-profile:hover{
    background-color: #0a16bd;
}


</style>