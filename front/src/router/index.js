import { createRouter, createWebHistory } from 'vue-router'
import Quizz from '@/pages/quizz/QuizzPage.vue'
const routes = [
  {
    path: '/',
    name: 'quizz',
    component: Quizz,
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
