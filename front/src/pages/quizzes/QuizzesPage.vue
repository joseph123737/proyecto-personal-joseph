<template>
    <h1 class="tittle">¿Que quizz quieres hacer?</h1>
    <div class="btn">
        <button class="btn-left" @click="goToAddNewQuizz">Añadir un quizz</button>
        <button class="btn-rigth" @click="goToViewUser">Ver mi perfil</button>
    </div>

    <div class="main">
        <div v-for="quizz of quizzes" :key="quizz.id_quizz">
        <router-link :to=" {name:'quizz',params:{id:quizz.id_quizz} }">
            <p class="btn-quizz">{{quizz.quizz_name}}</p>
        </router-link>
    </div>
  </div>
</template>

<script>
import {getAllQuizzes} from '@/services/api.js'
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
            let response =  await getAllQuizzes()
            this.quizzes =  await response.json()
        },
        goToAddNewQuizz(){
            this.$router.push({name:"add_new_quizz"})
        },
        goToViewUser(){
            const userJson = localStorage.getItem("auth");
            const user = JSON.parse(userJson);
            this.$router.push({name:"user",params:{id:user.user_id}})
        }

    },
}
</script>

<style scoped>
.main{
    display: grid;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
.btn{
    display: flex;
    justify-content: space-between;
}
.tittle{
    text-align: center;
}

.btn-quizz{
    background-color: #7209b7;
    padding: 0.5em;
    border: 2px solid #3d0563;
    border-radius:2em;
    color: white;
    max-width: 29em;
    padding: 0.8em 20em ;
    text-decoration: none;
    text-align: center;

}
.btn-quizz:hover{
background-color: #3d0563;
}

.btn-left{
    
    background-color: #f01066;
    padding: 0.5em;
  
    border: 2px solid #b40e4e;
    border-radius:2em;
    color: white;
}
.btn-left:hover{
    background-color: #b40e4e;
}

.btn-rigth{
    background-color: #0c1bee;
    padding: 0.5em;
    border: 2px solid #0a16bd;
    border-radius:2em;
    color: white;
}

.btn-rigth:hover{
    background-color: #0a16bd;
}

</style>