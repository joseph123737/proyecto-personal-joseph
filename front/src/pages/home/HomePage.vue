<template>
  <section>
      <h1 class="text">Bienvenido</h1>
  </section>
  <section class="form">
      <label for="username">introduzca su usuario</label>
      <input type="text" v-model="user.user_name" id="username">

      <label class="label-form"   for="password">introduzca su contraseña</label>
      <input type="password" v-on:keyup.enter="authenticationUser()" v-model="user.password" id="password">

      <button class="login-btn" @click="authenticationUser">logearse</button>
  </section>
  <router-link :to="{name:'new_user'}" class="text" >
  <p>no tienes un usuario clicka aqui</p>
  </router-link>
</template>

<script>
import {config} from '@/config.js'
import { useStorage } from "@vueuse/core";
export default {
    data(){
      return{
       user:{},
       auth: useStorage("auth", {}),
    }
  },
  methods:{
    checkIfTheInputAreEmpty(){
      if (this.user.user_name === "" ||
        this.user.password === "" ||
        this.user.user_name === undefined ||
        this.user.password === undefined
        ){
          return false

      }else{
          return true
      }
    },
    async authenticationUser(){
      const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(this.user),
    };
    if (this.checkIfTheInputAreEmpty()){
      const response = await fetch(`${config.AUTH_PATH}/login`, settings);
      if (response.status == 401){
        alert("unauthorize")
      }
      if (response.status == 404){
        alert("El usuario introducido no existe")
      }
      if (response.status == 200){
        const auth = await response.json();
        this.auth = auth;
        this.$router.push({name:"quizzes"})
      }
    }else{
      alert("comprueba si algun campo esta vacio")
    }
    },
    
  }

}
</script>

<style scoped>
.form{
  display: flex;
  flex-direction: column;
  max-width: 20em;
  margin: 3em auto 0;
  
}
.login-btn{
    background-color: #7209b7;
    padding: 0.5em;
    border: 2px solid #3d0563;
    border-radius:2em;
    color: white;
    text-decoration: none;
    margin-top: 2em;

}
.login-btn:hover{
  background-color: #3d0563;
}
.label-form{
  margin-top: 2em;
}
.text{
  text-align: center;
}

</style>