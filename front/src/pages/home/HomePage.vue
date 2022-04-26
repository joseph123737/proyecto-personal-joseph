<template>
  <section>
      <h1>Bienvenido a Proyecto Escorpion(temporal)</h1>
  </section>
  <section class="form">
      <label for="username">introduzca su usuario</label>
      <input type="text" v-model="user.user_id" id="username">

      <label for="password">introduzca su contraseña</label>
      <input type="password" v-model="user.password" id="password">

      <button class="login-btn" @click="authenticationUser">logearse</button>
  </section>
</template>

<script>
import { useStorage } from "@vueuse/core";
export default {
    data(){
      return{
       user:{},
       auth: useStorage("auth", {}),
    }
  },
  methods:{
    async authenticationUser(){
      const settings = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(this.user),
        

    };
    const response = await fetch("http://localhost:5000/auth/login", settings);
    if (response.status == 401){
      alert("unauthorize")
    }
    if (response.status == 200){
      const auth = await response.json();
      this.auth = auth;
      this.$router.push({name:"quizz"})
    }
    }
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
  border:2px solid #a31d1e;;
  padding: 1em;
  font-size: 0.9em;
  font-weight: bold;
  background-color:#a31d1e;
  color:rgb(247, 225, 181);
  margin-top: 1em;

}
.login-btn:hover{
  background-color: #771e1e;
}


</style>