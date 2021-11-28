import {
    Action,
    getModule,
    Module,
    Mutation,
    VuexModule,
} from 'vuex-module-decorators'

import store from '@/store'


@Module({dynamic: true, store, name: 'user'})
class User extends VuexModule{
    questions = []
    products = []
    user = null


    @Mutation
    setUser(value){
        this.user = value
    }

    @Mutation
    setProducts(value){
        this.products = value
    }

    @Mutation
    setQuestions(value){
        this.questions = value
    }
}


export const UserModule = getModule(User)
