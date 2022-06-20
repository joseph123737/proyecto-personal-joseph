<template>
<section class="main">
<h1>{{time}}</h1>
      <article v-for="i in filteredQuizz" :key="i.id" >
          <h3>{{i.question_quizz}}</h3>
          <article class="btn-answer">
          <input type="button" class="a"  @click="checkIfItIsCorrect(i.answer_01.is_correct,i.answer_01.id_button),checkGameIsFinish()" v-bind:class={true:correctMessage} :value="i.answer_01.title" id="1"/>
           <input type="button" class="a" @click="checkIfItIsCorrect(i.answer_02.is_correct,i.answer_02.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_1} :value="i.answer_02.title" id="2"/>
           <input type="button"  class="a" @click="checkIfItIsCorrect(i.answer_03.is_correct,i.answer_03.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_2} :value="i.answer_03.title" id="3"/>
           <input type="button" class="a" @click="checkIfItIsCorrect(i.answer_04.is_correct,i.answer_04.id_button),checkGameIsFinish()" v-bind:class={false:failedMessage_3} :value="i.answer_04.title" id="4"/>
          </article>
          <button v-if="goToNextQuizz" @click="nextQuizz" class="btn-next-quizz">siguiente quizz</button>
          <router-link v-if="showResult"  :to="{name:'result',params:{guest:countOfGuest,miss:countOfMiss}}">
          <button class="learn-more">
  <span class="circle" aria-hidden="true">
  <span class="icon arrow"></span>
  </span>
  <span class="button-text">Ver resultado</span>
</button>
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
            let response =  await fetch('http://192.168.0.10:5000/api/quizz/'+this.$route.params.id)
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
button {
 position: relative;
 display: inline-block;
 cursor: pointer;
 outline: none;
 border: 0;
 vertical-align: middle;
 text-decoration: none;
 background: transparent;
 padding: 0;
 font-size: inherit;
 font-family: inherit;
}

button.learn-more {
 width: 12rem;
 height: auto;
}

button.learn-more .circle {
 transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
 position: relative;
 display: block;
 margin: 0;
 width: 3rem;
 height: 3rem;
 background: #282936;
 border-radius: 1.625rem;
}

button.learn-more .circle .icon {
 transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
 position: absolute;
 top: 0;
 bottom: 0;
 margin: auto;
 background: #fff;
}

button.learn-more .circle .icon.arrow {
 transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
 left: 0.625rem;
 width: 1.125rem;
 height: 0.125rem;
 background: none;
}

button.learn-more .circle .icon.arrow::before {
 position: absolute;
 content: "";
 top: -0.29rem;
 right: 0.0625rem;
 width: 0.625rem;
 height: 0.625rem;
 border-top: 0.125rem solid #fff;
 border-right: 0.125rem solid #fff;
 transform: rotate(45deg);
}

button.learn-more .button-text {
 transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
 position: absolute;
 top: 0;
 left: 0.7em;
 right: 0;
 bottom: 0;
 padding: 0.75rem 0;
 margin: 0 0 0 1.85rem;
 color: #282936;
 font-weight: 700;
 line-height: 1.6;
 text-align: center;
 text-transform: uppercase;
}

button:hover .circle {
 width: 100%;
}

button:hover .circle .icon.arrow {
 background: #fff;
 transform: translate(1rem, 0);
}

button:hover .button-text {
 color: #fff;
}
.a{
    background-color: #7209b7;
    padding: 0.5em;
    border: 2px solid #3d0563;
    border-radius:2em;
    color: white;

}
.a:hover{
    background-color: #3d0563;
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