<template>
  <router-link :to="{name:'quizzes'}">
    <button class="btn-go-to-back">Volver a la seleccion de quizzes</button>
  </router-link>
  <header class="hd">
      <button @click="deleteAll" class="btn-delete-all">Borrar quizz</button>
      <button @click="openModal" class="btn-open-modal">Ver lista de quizzes</button>
      <button @click="finishForm" class="btn-finish-form" >Guardar quizz</button>
  </header>
  <main id="main">
      <input type="text" id="quizz_name" placeholder="escribe el nombre de tu quizz" v-model="quizz_name"/>
      <ul>
          <li><textarea class="principal-question" type="text" name="" id="principal_question" placeholder="escribe aqui tu pregunta" v-model="question_quizz" /></li>
          <li>Marca la casilla para decir cual es la correcta</li>
          <li>
              <input class="answer" type="text" name="" id="response_1" placeholder="escribe aqui tu respuesta" v-model="answer1Title">
              <input type="radio" name="radio" id="radio_01" value="1" v-model="is_correct">

          </li>
          <li>
              <input class="answer" type="text" name="" id="response_2" placeholder="escribe aqui tu respuesta" v-model="answer2Title">
              <input type="radio" name="radio" id="radio_02" value="2" v-model="is_correct">
           </li>
           <li>
              <input class="answer" type="text" name="" id="response_3" placeholder="escribe aqui tu respuesta" v-model="answer3Title">
              <input type="radio" name="radio" id="radio_03" value="3" v-model="is_correct">
           </li>
          <li>
              <input class="answer" type="text" name="" id="response_4" placeholder="escribe aqui tu respuesta" v-model="answer4Title">
              <input type="radio" name="radio" id="radio_04" value="4" v-model="is_correct">
          </li>
      </ul>
  </main>
    <AddNewQuizzModal v-if="modalOpened" :dictQuizz="quizzes" @changed="changeQuizzes" @modalToFalse="closeModal"/>
    <button @click="saveQuizzOnCollection" class="btn-add-to-colection" >Añadir a la coleccion</button>

</template>

<script>
import AddNewQuizzModal from "./addNewQuizzModal.vue";
import {saveNewQuizz} from "@/services/api.js"
export default {
    components:{
        AddNewQuizzModal
    },
    data(){
        return{
            question_quizz: "",
            answer1Title :"" ,
            answer2Title : "",
            answer3Title : "",
            answer4Title : "",
            is_correct:"",
            id:1,
            id_quizz:1,
            quizz_name : "",
            quizzes:[],
            modalOpened : false
        }
    },
    methods:{
        openModal(){
            this.modalOpened = true
        },
        closeModal(newValue){
            this.modalOpened = newValue
        },
        changeQuizzes(newValue){
            this.quizzes = newValue

        },
        vadilateSaveQuizz(quizz_name){
            if(
                quizz_name == undefined ||
                quizz_name == "")
            {
                return false
            }else{
 
                return true
            }
        },
        checkWhichOneIsCorrect(number){
            if (this.is_correct == number){
                return true 
            }else{
                return false
            }
        },
        async finishForm(){
            if (this.quizzes.length === 0){
                alert("no puedes guardar un quizz vacio, asegurate que as guardado tu quizz en la colecion")

            }else{
                let quizz_name = prompt("da un nombre a tu quizz")
                if (this.vadilateSaveQuizz(quizz_name)) {
                let response = await saveNewQuizz(this.quizzes,quizz_name)
                if (response.status == 200) {
                    this.$router.push({name:"quizzes"})
                }

            }
            }
        },
        autotificationQuizz(){
            if (this.quizz_name == "" ||
                this.question_quizz == "" || 
                this.answer1Title == "" || 
                this.answer2Title == "" || 
                this.answer3Title == "" || 
                this.answer4Title == ""){
                    return false
            }else{
                return true
            }
        },
        deleteAll(){
            this.quizz_name = ""
            this.question_quizz = ""
            this.answer1Title = ""
            this.answer2Title = ""
            this.answer3Title = ""
            this.answer4Title = ""

        },
        autetificationIfCheckedOneIsTrue(quizz){
            if (quizz.answer_01.is_correct == false &&
                quizz.answer_02.is_correct == false &&
                quizz.answer_03.is_correct == false &&
                quizz.answer_04.is_correct == false ){
                    return false
            }else{
                return true
            }
        },
        saveQuizzOnCollection(){
            if (this.autotificationQuizz()){
            let quizz_to_save = {
                id:this.id,
            question_quizz:this.question_quizz,
            answer_01 :{title:this.answer1Title,is_correct:this.checkWhichOneIsCorrect("1"),id_button:"1"},
            answer_02 :{title:this.answer2Title,is_correct:this.checkWhichOneIsCorrect("2"),id_button:"2"},
            answer_03 :{title:this.answer3Title,is_correct:this.checkWhichOneIsCorrect("3"),id_button:"3"},
            answer_04 :{title:this.answer4Title,is_correct:this.checkWhichOneIsCorrect("4"),id_button:"4"}
            }
            if (this.autetificationIfCheckedOneIsTrue(quizz_to_save)){
                this.quizzes.push(quizz_to_save)
                this.id+=1
                this.id_quizz+= 1
                this.quizz_name = ""
                this.question_quizz = ""
                this.answer1Title = ""
                this.answer2Title = ""
                this.answer3Title = ""
                this.answer4Title = ""
            }else{
                alert("Seleccione una respuesta correcta")
            }
        }else{
            alert("Revisa si no hay ningun campo del formulario en blaco")
        }
    }
    }
}
</script>

<style scoped>


*{
    margin: 0;
    padding: 0;
}

.btn-go-to-back{
    margin: 0.5em;
    text-align: center;
    background-color: #7209b7;
    padding: 0.5em;
    border: 2px solid #3d0563;
    border-radius:2em;
    color: white;
    text-decoration: none;
}
.btn-go-to-back:hover{
    background-color: #3d0563;
}

.principal-question{
    margin: 0.5em;
    text-align: center;
    background-color: #fc0796;
    padding: 0.5em;
    border: 2px solid #e70c8c;
    border-radius:2em;
    color: white;
}

.hd{
  display: flex;
  justify-content: space-between;
}
ul{
    list-style: none;
}
#quizz_name{
    margin-top: 2em;
    text-align: center;
    max-width: 17em;
    background-color: #fc0796;
    padding: 0.5em;
    border: 2px solid #e70c8c;
    border-radius:2em;
    color: white;
}
.answer{
    margin: 0.5em;
    text-align: center;
    background-color: #eb0b8d;
    padding: 0.5em;
    border: 2px solid #e70c8c;
    border-radius:2em;
    color: white;
}
#main{
    display: grid;
    grid-template-columns: 1fr ,1fr;
    align-content: center;
    justify-content: center;

}
#principal_question{
    text-align: center;
    max-height: 15em;
    min-height: 15em;
    max-width: 17em;
    min-width: 17em;
    padding: 2em 1.5em;
    margin: 2em 0;
}
.btn-add-to-colection{
   margin: auto;
   display: flex;
   justify-items: center;
   align-items: center;
   background-color: #e66d0a;
   padding: 0.5em;
   border: 2px solid #bb5807;
   border-radius:2em;
   color: white;
   margin-top: 1em;
}

.btn-add-to-colection:hover{
    background-color: #bb5807;

}

.btn-finish-form{
   background-color: rgb(16, 218, 16);
   padding: 0.5em;
   border: 2px solid rgb(12, 184, 12);
   border-radius:2em;
   color: white;
   margin-top: 1em;
}

.btn-finish-form:hover{
    background-color: rgb(12, 184, 12);
}

.btn-open-modal{
   background-color: #74eb04;
   padding: 0.5em;
   border: 2px solid #60c007;
   border-radius:2em;
   color: white;
   margin-top: 1em; 
}
.btn-open-modal:hover{
    background-color: #60c007;
}

.btn-delete-all{
   background-color: #f50909;
   padding: 0.5em;
   border: 2px solid #c50606;
   border-radius:2em;
   color: white;
   margin-top: 1em;

}
.btn-delete-all:hover{
    background-color:#c50606;
}

</style>
