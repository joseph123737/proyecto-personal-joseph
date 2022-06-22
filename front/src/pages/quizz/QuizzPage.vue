<template>
<section class="main">
<h1>{{time}}</h1>
      <article v-for="i in filteredQuizz" :key="i.id" >
          <h3>{{i.question_quizz}}</h3>
          <article class="btn-answer">
           <input type="button" class="btn-text"  @click="checkIfItIsCorrect(i.answer_01.is_correct,i.answer_01.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_1,true:correctMessage_01} :value="i.answer_01.title" id="1"/>
           <input type="button" class="btn-text" @click="checkIfItIsCorrect(i.answer_02.is_correct,i.answer_02.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_2,true:correctMessage_02} :value="i.answer_02.title" id="2"/>
           <input type="button"  class="btn-text" @click="checkIfItIsCorrect(i.answer_03.is_correct,i.answer_03.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_3,true:correctMessage_03} :value="i.answer_03.title" id="3"/>
           <input type="button" class="btn-text" @click="checkIfItIsCorrect(i.answer_04.is_correct,i.answer_04.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_4,true:correctMessage_04} :value="i.answer_04.title" id="4"/>
          </article>
        </article>
</section>
<div class="btn-go">
          <button v-if="goToNextQuizz"  @click="nextQuizz" class="btn-next-quizz">Siguiente quizz</button>
          <router-link v-if="showResult"  :to="{name:'result',params:{guest:countOfGuest,miss:countOfMiss}}">
          <button class="btn-check-result">Ver resultado</button>
          </router-link>
</div>
</template>

<script>
import {getQuizzById} from '@/services/api.js'
export default {
    data(){
        return{
        quizzes : {},
        failedMessage_1 : false,
        failedMessage_2:false,
        failedMessage_3:false,
        failedMessage_4:false,
        correctMessage_01 : false,
        correctMessage_02 : false,
        correctMessage_03 : false,
        correctMessage_04 : false,
        goToNextQuizz:false,
        showResult : false,
        stopChrono : false,
        time:30,
        numberOfQuizz : 1,
        filteredQuizz:[],
        countOfGuest :0,
        countOfMiss: 0

        }
    },
    mounted(){
        this.loadData()
        this.chronometer()
        },
    methods:{ 
        async loadData(){
            let response =  await getQuizzById(this.$route.params.id)
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
            this.stopChrono = true
            
        },
        filterQuizz(){
            this.filteredQuizz = this.quizzes.quizzes.filter((i) => i.id ===this.numberOfQuizz)
            
        },
        nextQuizz(){
            this.numberOfQuizz++
            this.correctMessage_01 = false
            this.correctMessage_02 = false
            this.correctMessage_03 = false
            this.correctMessage_04 = false
            this.stopChrono = false
            this.failedMessage_1 = false
            this.failedMessage_2 = false
            this.failedMessage_3 = false
            this.failedMessage_4 = false
            this.time = 30
            this.goToNextQuizz = false
            this.filterQuizz()
        },
        chronometer(){
             setInterval(()=>{
                
                if (this.stopChrono == false){
                        if (this.time > 0){
                            this.time--
                        }
                        
                        if (this.time == 0){
                            this.time= "se acabo el tiempo"
                            this.findTheCorrect()
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
        findTheCorrect(){
            for (let i of this.filteredQuizz){
                if(i.answer_01.is_correct == true){
                    this.correctMessage_01 = true
                }
                if(i.answer_02.is_correct == true){
                    this.correctMessage_02 = true
                }
                if(i.answer_03.is_correct == true){
                    this.correctMessage_03 = true
                }
                if(i.answer_04.is_correct == true){
                    this.correctMessage_04 = true
                }
            }
        },
        findTheButtonPress(id_button){
            if (id_button == "1"){
                this.failedMessage_1= true
            }
            if (id_button == "2"){
                this.failedMessage_2 = true
            }
            if (id_button == "3"){
                this.failedMessage_3 = true
            }
            if (id_button == "4"){
                this.failedMessage_4 = true
            }

        },
        checkIfItIsCorrect(answer,id_button){
            if (answer === true){
                this.countOfGuest++
                this.findTheCorrect()
                this.disabledTheButton()
            }
            if (answer === false) {
                this.countOfMiss++
                this.findTheButtonPress(id_button)
                this.findTheCorrect()
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
.btn-go{
    display: flex;
    align-content: center;
    justify-content: center;
}


.btn-check-result{
    background-color: #e60aaf;
    padding: 0.5em;
    border: 2px solid #a80780;
    border-radius:2em;
    color: white;
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
.false:hover{
    background-color:  rgb(150, 12, 12);
}
.true{
    background-color:  rgb(6, 90, 6);
}
.true:hover{
    background-color:  rgb(6, 90, 6);
}

.true_2{
    background-color:  rgb(6, 90, 6);
}
.true_2:hover{
    background-color:  rgb(6, 90, 6);
}


</style>