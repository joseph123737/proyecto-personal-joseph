<template>
  <h1>¿Que quizz quieres hacer?</h1>
  <div v-for="quizz of quizzes" :key="quizz.id_quizz">
  <router-link :to=" {name:'quizz',params:{id:quizz.id_quizz} }">
    <p>{{quizz.quizz_name}}</p>
  </router-link>
  </div>
</template>

<script>
export default {
    data(){
        return{
            quizzes:[]

        }
    },
    mounted(){
        this.loadData()
    },
    methods:{
        async loadData(){
            let response =  await fetch('http://192.168.21.143:5000/api/quizz')
            this.quizzes =  await response.json()
        }
    },
}
</script>

<style>

</style>