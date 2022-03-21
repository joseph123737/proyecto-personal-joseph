<template>
<h1>{{time}}</h1>
  <div v-for="quizz in quizzes" :key="quizz.id_quizz">
      <h1>{{quizz.quizz_name}}</h1>
      <section v-for="i in quizz.quizz" :key="i.id" >
          <h3>{{i.question_quizz}}</h3>
          <article class="botton-answer">
          <input type="button" @click="checkIfItIsCorrect(i.answer_01.is_correct,i.answer_01.id_button)" v-bind:class={true:correctMessage} :value="i.answer_01.title" id="1"/>
           <input type="button" @click="checkIfItIsCorrect(i.answer_02.is_correct,i.answer_02.id_button)" v-bind:class={false:failedMessage_1} :value="i.answer_02.title" id="2"/>
           <input type="button" @click="checkIfItIsCorrect(i.answer_03.is_correct,i.answer_03.id_button)" v-bind:class={false:failedMessage_2} :value="i.answer_03.title" id="3"/>
           <input type="button" @click="checkIfItIsCorrect(i.answer_04.is_correct,i.answer_04.id_button)" v-bind:class={false:failedMessage_3} :value="i.answer_04.title" id="4"/>
          </article>
      </section>

  </div>
</template>

<script>
export default {
    data(){
        return{
            quizzes : [{
id_quizz: "01",
quizz_name :"prueba uno",
quizz: [
           {id : 1,
            question_quizz : "que hace la siguiente list comprehension :  [( i) for i in range (5) ]",
            answer_01 : {title: "hace un for del 1 al 5", is_correct: true,id_button:"1"},
            answer_02 : {title: "esta no", is_correct: false,id_button:"2"},
            answer_03 : {title: "esta tampoco", is_correct: false,id_button:"3"},
            answer_04 : {title: "empieza a leer de nuevo", is_correct: false,id_button:"4"},
          
           },
           ]
          }],
        failedMessage_1 : false,
        failedMessage_2:false,
        failedMessage_3:false,
        correctMessage : false,
        time:3

        }
    },
    mounted(){
/*        this.chronometer() */
        },
    methods:{
/*        chronometer(){
             setInterval(()=>{
                
            if (this.time > 0){
                this.time--
            }
            if (this.time == 0){
                this.time= "jeff"
                this.correctMessage = true
            }    
            },1000)
        }, */
        checkIfItIsCorrect(answer,id_button){
            if (answer === true){
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