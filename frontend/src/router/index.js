import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/pages/register',
    },
    {
        path: '/pages/register',
        name: 'pages-register',
        component: () => import('@/pages/Register.vue'),
    },
    {
        path: '/pages/login',
        name: 'pages-login',
        component: () => import('@/pages/Login.vue'),
    },
    {
        path: '/pages/questions',
        name: 'pages-questions',
        component: () => import('@/pages/Questions.vue')
    },
    {
        path: '/pages/products',
        name: 'pages-products',
        component: () => import('@/pages/Products.vue')
    },
    {
        path: '/error-404',
        name: 'error-404',
        component: () => import('@/views/Error.vue'),
    },
    {
        path: '/*',
        redirect: 'error-404',
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
})

export default router
