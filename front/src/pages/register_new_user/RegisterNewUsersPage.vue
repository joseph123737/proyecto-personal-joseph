<template>
<section class="form">
  <label for="userName">Nombre de usuario: </label>
  <input type="text"  id="userName" v-model="newUser.user_name">

  <label for="password" class="input-form">Contraseña: </label>
  <input type="text" id="password" v-on:keyup.enter="sendNewUser()" v-model="newUser.password">
</section>
  <button class="login-btn" >Registrase</button>
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
            console.log(config.API_PATH)
            var response = await fetch(`${config.API_PATH}/users/login-users/add-new-user`, settings);
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