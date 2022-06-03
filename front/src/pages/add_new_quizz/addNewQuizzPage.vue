<template>
  <header class="hd">
      <button>borrar todo</button>
      <button>acabar</button>
      <button>añadir a la coleccion</button>
  </header>
  <main>
      <ul>
          <li><textarea type="text" name="" id="principal_question" placeholder="escribe aqui tu pregunta" /></li>
          <li><input class="answer" type="text" name="" id="response_1" placeholder="escribe aqui tu respuesta"></li>
          <li><input class="answer" type="text" name="" id="response_2" placeholder="escribe aqui tu respuesta"></li>
          <li><input class="answer" type="text" name="" id="response_3" placeholder="escribe aqui tu respuesta"></li>
          <li><input class="answer" type="text" name="" id="response_4" placeholder="escribe aqui tu respuesta"></li>
      </ul>
  </main>
</template>

<script>
export default {

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
.answer{
    margin: 0.5em;
    text-align: center;
}
#principal_question{
    text-align: center;
    max-height: 15em;
    min-height: 15em;
    max-width: 17em;
    min-width: 17em;
    padding: 2em 1.5em;
    margin: 2em;
}
</style>