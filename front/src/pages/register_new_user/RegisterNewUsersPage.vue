<template>
<section class="form">
  <label for="userName">Nombre de usuario: </label>
  <input type="text"  id="userName" v-model="newUser.user_name">

  <label class="label-form" for="password">Contraseña: </label>
  <input type="text" id="password" v-on:keyup.enter="sendNewUser()" v-model="newUser.password">
  <button class="login-btn" @click="sendNewUser">Registrase</button> 
</section>
</template>

<script>
import { v4 as uuidv4 } from "uuid";
import {config} from '@/config.js'
export default {
    data(){
        return{
            newUser:{
                password : "",
                user_name : ""
            }
        }
    },
    methods:{
        async sendNewUser(){
            this.newUser.user_id = uuidv4()
            const settings = {
                method: "POST",
                body: JSON.stringify(this.newUser),
                headers: {
                    "Content-Type": "application/json",
                },
                };
            var response = await fetch(`${config.API_PATH}/users/login-users/add-new-user`, settings);
            if (response.status == 409){
                alert("Ese usuario ya existe")
            }
            if (response.status == 200){
                alert("usuario añadido con exitosamente")
                this.$router.push({name:"home"})
            }

             

        }
    },
}
</script>

<style>
.form{
  display: flex;
  flex-direction: column;
  max-width: 20em;
  margin: 3em auto 0;
}
.input-form {
    margin-top: 1.3em;
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


 
</style>