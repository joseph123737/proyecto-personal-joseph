import { createRouter, createWebHistory } from 'vue-router'
import Quizz from '@/pages/quizz/QuizzPage.vue'
import Result from '@/pages/result/ResultPage.vue'
const routes = [
  {
    path: '/',
    name: 'quizz',
    component: Quizz,
  },
  {
    path : '/result',
    name:'result',
    component : Result
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
