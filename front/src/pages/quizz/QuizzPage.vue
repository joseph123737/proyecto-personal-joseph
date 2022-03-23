<template>
<section v-if="startGameButton">
    <button @click="startGame">empezar juego</button>

</section>
<section v-if="quizzContinued">
<h1>{{time}}</h1>
      <article v-for="i in filteredQuizz" :key="i.id" >
          <h3>{{i.question_quizz}}</h3>
          <article class="botton-answer">
          <input type="button" @click="checkIfItIsCorrect(i.answer_01.is_correct,i.answer_01.id_button),checkGameIsFinish()" v-bind:class={true:correctMessage} :value="i.answer_01.title" id="1"/>
           <input type="button" @click="checkIfItIsCorrect(i.answer_02.is_correct,i.answer_02.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_1} :value="i.answer_02.title" id="2"/>
           <input type="button"  @click="checkIfItIsCorrect(i.answer_03.is_correct,i.answer_03.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_2} :value="i.answer_03.title" id="3"/>
           <input type="button"  @click="checkIfItIsCorrect(i.answer_04.is_correct,i.answer_04.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_3} :value="i.answer_04.title" id="4"/>
          </article>
          <button v-if="nextQuizzBoolean" @click="nextQuizzButton">siguiente quizz</button>
          <button v-if="finishGameButton" @click="FinishGame">ver resultado</button>
      </article>
</section>
<section v-if="finishGame">
    <h2>As acertado: {{countOfGues}} de {{quizzes.quizz.length}}</h2>
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
        nextQuizzBoolean:false,
        filteredQuizz:[],
        finishGame : false,
        finishGameButton : false,
        quizzContinued:false,
        countOfGues :0,
        startGameButton : true

        }
    },
    mounted(){
        this.loadData()
        this.chronometer() 
        },
    methods:{
        async loadData(){
            let response =  await fetch('http://192.168.21.143:5000/api/quizz')
            this.quizzes =  await response.json()
        },
        startGame(){
            this.startGameButton = false
            this.quizzContinued = true
            this.filterQuizz()
        },
        FinishGame(){
            this.quizzContinued = false
            this.finishGame = true
        },
        checkGameIsFinish(){
            if (this.quizzes.quizz.length === this.numberOfQuizz){
                this.finishGameButton = true
            }
            if(this.quizzes.quizz.length !== this.numberOfQuizz){
                this.nextQuizzBoolean = true
            }
        },
        filterQuizz(){
            this.filteredQuizz = this.quizzes.quizz.filter((i) => i.id ===this.numberOfQuizz)
            
        },
        nextQuizzButton(){
            this.numberOfQuizz++
            this.correctMessage = false
            this.failedMessage_1 = false
            this.failedMessage_2 = false
            this.failedMessage_3 = false
            this.time = 30
            this.nextQuizzBoolean = false
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

                        }
                }    
            },1000)
        }, 
        checkIfItIsCorrect(answer,id_button){
            if (answer === true){
                this.countOfGues++
                this.correctMessage = true
                document.getElementById("2").disabled = true
                document.getElementById("3").disabled = true
                document.getElementById("4").disabled = true
            }
            if (answer === false && id_button ==="2") {
                this.failedMessage_1 = true
                this.correctMessage = true
                document.getElementById("3").disabled = true
                document.getElementById("4").disabled = true

            }
            if (answer === false && id_button ==="3") {
                this.failedMessage_2 = true
                this.correctMessage = true
                document.getElementById("2").disabled = true
                document.getElementById("4").disabled = true
            }
            if (answer === false && id_button ==="4") {
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