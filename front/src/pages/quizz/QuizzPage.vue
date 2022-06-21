<template>
<section class="main">
<h1>{{time}}</h1>
      <article v-for="i in filteredQuizz" :key="i.id" >
          <h3>{{i.question_quizz}}</h3>
          <article class="btn-answer">
          <input type="button" class="btn-text"  @click="checkIfItIsCorrect(i.answer_01.is_correct,i.answer_01.id_button),checkGameIsFinish()" v-bind:class={true:correctMessage} :value="i.answer_01.title" id="1"/>
           <input type="button" class="btn-text" @click="checkIfItIsCorrect(i.answer_02.is_correct,i.answer_02.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_1} :value="i.answer_02.title" id="2"/>
           <input type="button"  class="btn-text" @click="checkIfItIsCorrect(i.answer_03.is_correct,i.answer_03.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_2} :value="i.answer_03.title" id="3"/>
           <input type="button" class="btn-text" @click="checkIfItIsCorrect(i.answer_04.is_correct,i.answer_04.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_3} :value="i.answer_04.title" id="4"/>
          </article>
          <button v-if="goToNextQuizz"  @click="nextQuizz" class="btn-next-quizz">siguiente quizz</button>
          <router-link v-if="showResult"  :to="{name:'result',params:{guest:countOfGuest,miss:countOfMiss}}">
          <button class="btn-check-result">Ver resultado</button>
          </router-link>
        </article>
</section>
</template>

<script>
import {config} from '@/config.js'
export default {
    data(){
        return{
        quizzes : {},
        failedMessage_1 : false,
        failedMessage_2:false,
        failedMessage_3:false,
        correctMessage : false,
        time:30,
        numberOfQuizz : 1,
        goToNextQuizz:false,
        filteredQuizz:[],
        finishGame : false,
        quizzContinued:false,
        countOfGuest :0,
        countOfMiss: 0,
        showResult : false

        }
    },
    mounted(){
        this.loadData()
        this.chronometer()
        },
    methods:{ 
        async loadData(){
            let response =  await fetch(`${config.API_PATH}/quizz/${this.$route.params.id}`)
            this.quizzes =  await response.json()
            this.filterQuizz()
        },
        checkGameIsFinish(){
            if (this.quizzes.quizzes.length === this.numberOfQuizz){
                this.showResult = true
            }
            if(this.quizzes.quizzes.length !== this.numberOfQuizz){
                this.goToNextQuizz = true
            }
        },
        filterQuizz(){
            this.filteredQuizz = this.quizzes.quizzes.filter((i) => i.id ===this.numberOfQuizz)
            
        },
        nextQuizz(){
            this.numberOfQuizz++
            this.correctMessage = false
            this.failedMessage_1 = false
            this.failedMessage_2 = false
            this.failedMessage_3 = false
            this.time = 30
            this.goToNextQuizz = false
            this.filterQuizz()
        },
        chronometer(){
             setInterval(()=>{
                
                if (this.correctMessage === false){
                        if (this.time > 0){
                            this.time--
                        }
                        
                        if (this.time == 0){
                            this.time= "se acabo el tiempo"
                            this.correctMessage = true
                            document.getElementById("2").disabled = true
                            document.getElementById("3").disabled = true
                            document.getElementById("4").disabled = true
                            this.countOfMiss++
                            this.checkGameIsFinish()

                        }
                }    
            },1000)
            
        }, 
        disabledTheButton(){
            document.getElementById("1").disabled = true
            document.getElementById("2").disabled = true
            document.getElementById("3").disabled = true
            document.getElementById("4").disabled = true
        },
        checkIfItIsCorrect(answer,id_button){
            if (answer === true){
                this.countOfGuest++
                this.correctMessage = true
                this.disabledTheButton()
            }
            if (answer === false && id_button ==="2") {
                this.countOfMiss++
                this.failedMessage_1 = true
                this.correctMessage = true
                this.disabledTheButton()

            }
            if (answer === false && id_button ==="3") {
                this.countOfMiss++
                this.failedMessage_2 = true
                this.correctMessage = true
                this.disabledTheButton()
            }
            if (answer === false && id_button ==="4") {
                this.countOfMiss++
                this.failedMessage_3 = true
                this.correctMessage = true
                this.disabledTheButton()
            }
        }
    }

}

</script>

<style scoped>
.btn-answer{
    display: grid;
    grid-template-columns: 1fr ;
    padding: 0 15%;

}

.btn-text{
    background-color: #7209b7;
    padding: 0.5em;
    border: 2px solid #3d0563;
    border-radius:2em;
    color: white;

}
.btn-text:hover{
    background-color: #3d0563;
}


.btn-check-result{
    background-color: #e60aaf;
    padding: 0.5em;
    border: 2px solid #a80780;
    border-radius:2em;
    color: white;
    margin-left: 17em;
    margin-top: 1em;

}
.btn-check-result:hover{
    background-color: #a80780;
}


.btn-next-quizz{
    background-color: #d80947;
    padding: 0.5em;
    border: 2px solid #a00836;
    border-radius:2em;
    color: white;
    margin-left: 17em;
    margin-top: 1em;
}
.btn-next-quizz:hover{
    background-color: #a00836;
}


.main{
    display: flex;
    justify-content: center;
    flex-direction: column;
    color: #282936;
    align-items: center;
    
}

.false{
    background-color:  rgb(150, 12, 12);
}  
.true{
    background-color:  rgb(6, 90, 6);
}

</style>