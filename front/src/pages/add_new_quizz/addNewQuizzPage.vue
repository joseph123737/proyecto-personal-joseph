<template>
  <header class="hd">
      <button @click="deleteAll">Borrar quizz</button>
      <button @click="openModal">Ver lista de quizzes</button>
      <button @click="saveQuizzOnCollection">Añadir a la coleccion</button>
  </header>
  <main id="main">
      <input type="text" id="quizz_name" placeholder="escribe el nombre de tu quizz" v-model="quizz_name"/>
      <ul>
          <li><textarea type="text" name="" id="principal_question" placeholder="escribe aqui tu pregunta" v-model="question_quizz" /></li>
          <li><input class="answer" type="text" name="" id="response_1" placeholder="escribe aqui tu respuesta" v-model="answer1Title"></li>
          <li><input class="answer" type="text" name="" id="response_2" placeholder="escribe aqui tu respuesta" v-model="answer2Title"></li>
          <li><input class="answer" type="text" name="" id="response_3" placeholder="escribe aqui tu respuesta" v-model="answer3Title"></li>
          <li><input class="answer" type="text" name="" id="response_4" placeholder="escribe aqui tu respuesta" v-model="answer4Title"></li>
      </ul>
  </main>
    <AddNewQuizzModal v-if="modalOpened" :dictQuizz="quizzes" @changed="changeQuizzes" @modalToFalse="closeModal"/>
  <button @click="finishForm" class="btn_finish_form">Guardar quizz</button>
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
                quizz_name == "" ||
                this.quizzes == [])
            {
                return false
            }else{
                return true
            }
        },
        async finishForm(){
            let quizz_name = prompt("da un nombre a tu quizz")
            if (this.vadilateSaveQuizz(quizz_name)) {
                let response = await saveNewQuizz(this.quizzes,quizz_name)
                if (response == 200) {

                    this.$route.push({name:"home"})

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
        saveQuizzOnCollection(){
            if (this.autotificationQuizz()){
            let quizz_to_save = {
            id_quizz: this.id_quizz,
            quizz_name:this.quizz_name, 
            quizz: {
                id:this.id,
                question_quizz:this.question_quizz,
                answer_1 :{title:this.answer1Title,is_true:false,id_button:"1"},
                answer_2 :{title:this.answer2Title,is_true:false,id_button:"2"},
                answer_3 :{title:this.answer3Title,is_true:false,id_button:"3"},
                answer_4 :{title:this.answer4Title,is_true:false,id_button:"4"}
                }
            
            }
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
}
.answer{
    margin: 0.5em;
    text-align: center;
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
.btn_finish_form{
   margin: auto;
   display: flex;
   justify-items: center;
   align-items: center;
}
</style>