<template>
    <main class="modal-wrapper">
        <section class="modal-inner-wrapper">
            <button class="close-btn" @click="closeModal">x</button>
            <div class="patat" v-for="quizz in dict_quizz" :key="quizz.id_quizz" >
                <p class="pa">{{quizz.quizz_name}}</p>
                <button @click="deleteQuizz(quizz)">x</button>
            </div>
        </section>
    </main>
</template>

<script>

export default {
    props:{
        dictQuizz:{
            type: Object,
            required : true,
        }
    },
    watch:{
        dictQuizz: {
            handler(newValue){
                let quizzAsJson = JSON.stringify(newValue)
                console.log(newValue) 
                return JSON.parse(quizzAsJson)

            },
        }
    },
    emits:["changed","modalToFalse"],
    data(){
        return{
            dict_quizz: this.dictQuizz,
            modalOpened: true
        }
    },
    
    methods:{
        deleteQuizz(quizz){
            let index = this.dict_quizz.indexOf(quizz)
            this.dict_quizz.splice(index,1)
            this.$emit("changed",this.dict_quizz)
        },
        closeModal(){
            this.modalOpened = false    
            this.$emit("modalToFalse",this.modalOpened)
        },
    }

}
</script>

<style scoped>

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.modal-wrapper{
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(250, 246, 246, 0.589);
    position: fixed;
    top: 0;
    left:0;
    z-index: 999;

}
.modal-inner-wrapper{
    width:70%;
    display: flex;
    flex-direction: column;
    background-color: rgb(14, 197, 230);
    padding: 1em 1em 3em;
    color:#fae8b9;
}
.patat{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.pa{
    font-size: 1.2em;
    margin-top: 0.5em;
    font-weight: bold;
} 
.close-btn {
    color:#a31d1e;
    background-color:#fae8b9;
    width: 25px;
    height: 25px;
    display: flex;
    justify-content: center;
    align-items: center;
    align-self: flex-end;
}

</style>

