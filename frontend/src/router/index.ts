import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Article from '../views/Article.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/article/:id',
      name: 'article',
      component: Article,
      props: true
    }
  ]
})

export default router 