import { createRouter, createWebHistory } from 'vue-router'
import Quizz from '@/pages/quizz/QuizzPage.vue'
import Result from '@/pages/result/ResultPage.vue'
import User from '@/pages/user/UserPage.vue'
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
  {
    path:'/user',
    name:'user',
    component:User
  },
  

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
