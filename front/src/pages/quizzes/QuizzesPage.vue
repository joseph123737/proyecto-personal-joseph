<template>
    <h1 class="tittle">¿Que quizz quieres hacer?</h1>
    <div class="btn">
        <button @click="goToAddNewQuizz">Añadir un quizz</button>
        <button @click="goToViewUser">Ver mi perfil</button>
    </div>

    <div class="main">
        <div v-for="quizz of quizzes" :key="quizz.id_quizz">
        <router-link :to=" {name:'quizz',params:{id:quizz.id_quizz} }">
            <p>{{quizz.quizz_name}}</p>
        </router-link>
    </div>
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
            let response =  await fetch('http://192.168.0.10:5000/api/quizz')
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
    display: flex;
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
</style>