<template>
<section>
<h1>{{time}}</h1>
      <article v-for="i in filteredQuizz" :key="i.id" >
          <h3>{{i.question_quizz}}</h3>
          <article class="botton-answer">
          <input type="button" @click="checkIfItIsCorrect(i.answer_01.is_correct,i.answer_01.id_button),checkGameIsFinish()" v-bind:class={true:correctMessage} :value="i.answer_01.title" id="1"/>
           <input type="button" @click="checkIfItIsCorrect(i.answer_02.is_correct,i.answer_02.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_1} :value="i.answer_02.title" id="2"/>
           <input type="button"  @click="checkIfItIsCorrect(i.answer_03.is_correct,i.answer_03.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_2} :value="i.answer_03.title" id="3"/>
           <input type="button"  @click="checkIfItIsCorrect(i.answer_04.is_correct,i.answer_04.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_3} :value="i.answer_04.title" id="4"/>
          </article>
          <button v-if="goToNextQuizz" @click="nextQuizz">siguiente quizz</button>
          <router-link v-if="showResult" :to="{name:'result',params:{guest:countOfGuest,miss:countOfMiss}}">
          <button>ver resultado</button>
          </router-link>
      </article>
</section>
</template>

<script>
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
            let response =  await fetch('http://192.168.21.143:5000/api/quizz/'+this.$route.params.id)
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
        checkIfItIsCorrect(answer,id_button){
            if (answer === true){
                this.countOfGuest++
                this.correctMessage = true
                document.getElementById("2").disabled = true
                document.getElementById("3").disabled = true
                document.getElementById("4").disabled = true
            }
            if (answer === false && id_button ==="2") {
                this.countOfMiss++
                this.failedMessage_1 = true
                this.correctMessage = true
                document.getElementById("3").disabled = true
                document.getElementById("4").disabled = true

            }
            if (answer === false && id_button ==="3") {
                this.countOfMiss++
                this.failedMessage_2 = true
                this.correctMessage = true
                document.getElementById("2").disabled = true
                document.getElementById("4").disabled = true
            }
            if (answer === false && id_button ==="4") {
                this.countOfMiss++
                this.failedMessage_3 = true
                this.correctMessage = true
                document.getElementById("2").disabled = true
                document.getElementById("3").disabled = true
            }
        }
    }

}

</script>

<style>
.botton-answer{
    display: grid;
    grid-template-columns: 1fr ;
    padding: 0 15%;

}
.false{
    background-color:  crimson;
}
.true{
    background-color:  green;
}

</style>