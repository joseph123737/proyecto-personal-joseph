<template>
  <main class="main">

    <ul>

      <li>
        As acertado : 
        <h1>{{user.quizz_guest}}</h1>
      </li>

      <li>
        As fallado : 
        <h1>{{user.quizz_miss}}</h1>
      </li>

      <li>
        Porcentaje de aciertos : 
        <h1>{{calculatedPercentOfGuest()}}%</h1>
      </li>

    </ul>
    <router-link :to="{name:'quizzes'}">
      <button class="btn-back-to-select-quizz">Volver a seleccionar quizz</button>
    </router-link>

  </main>
</template>

<script>
import {getUserStatsById} from '@/services/api.js'
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
        let response =  await getUserStatsById(this.$route.params.id)
        this.user =  await response.json()
    },
    calculatedPercentOfGuest(){
      if(this.user.quizz_guest == "0"){
        return 0 
      }
      if (this.user.quizz_miss == "0"){
          return 100 
      }else{
         let total  = parseInt(this.user.quizz_guest) + parseInt(this.user.quizz_miss)
          let  percent = parseInt(this.user.quizz_guest) / total

          return percent * 100
      }
    }
  },

}
</script>

<style scoped>

li{
  list-style: none ;
}
.main{ 
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-items: center;
}

.btn-back-to-select-quizz{
    background-color: #7209b7;
    padding: 0.5em;
    border: 2px solid #3d0563;
    border-radius:2em;
    color: white;
    text-decoration: none;
}
.btn-back-to-select-quizz:hover{
  background-color: #3d0563;
}
</style>