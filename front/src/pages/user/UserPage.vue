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

  </main>
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
</style>