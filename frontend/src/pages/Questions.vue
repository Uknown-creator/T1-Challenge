<template>
    <div class="auth-wrapper auth-v1">
        <div class="auth-inner">
            <QuestionItem
                @next_question="nextQuestion"
                :src="currentQuestion.src"
                :currentNumber="questionNumber"
                :length="UserModule.questions.length"
                header='Посмотрите несколько секунд на картинку и нажмите "Продолжить".'
                class="questions-item"
            />
        </div>
        <v-img
            class="auth-tree"
            width="100%"
            height="100%"
            src="@/assets/images/custom/questions-background.jpeg"
        ></v-img>
    </div>
</template>

<script>
import { isLoading, useApi, useCamera, useLoader } from '@/utils'
import {ref, computed, watch} from "@vue/composition-api"
import QuestionItem from "@/components/QuestionItem.vue"
import {prodPhoto} from '@/components/scanHelpers'
import {UserModule} from '@/store/questions'

export default {
    components: {
        QuestionItem
    },

    setup(props, {root}){
        const questionNumber = ref(0)
        const resultsData = ref([])
        const loader = useLoader()


        const sendDataToServer = () => {
            loader.show()
            const {exec, result, error} = useApi({
                method: "POST",
                url: "/insert_questions",
                data: {
                    listBase64im: resultsData
                }
            }, {loading: false})
            exec()

            setTimeout(() => {
                root.$router.push({"name": "pages-products"})
                loader.hide()
            }, 2000)

            watch(result, () => {
                if (result.value){
                    // UserModule.setProducts(result.value)
                    UserModule.setProducts(prodPhoto)
                    console.log(UserModule.products)
                }
            })

            result.value = prodPhoto
        }


        const currentQuestion = computed(() => {
            return UserModule.questions[questionNumber.value]
        })

        const savePhoto = () => {
            const {exec, result} = useCamera()
            exec()

            resultsData.value[questionNumber.value] = result.value
        }


        const nextQuestion = () => {
            savePhoto()
            if (questionNumber.value + 1 < UserModule.questions.length) {
                questionNumber.value++
            } else {
                console.log(resultsData.value)
                sendDataToServer()
            }
        }
        console.log(UserModule.questions)

        return {
            questionNumber,
            UserModule,
            currentQuestion,
            nextQuestion
        }
    }
}
</script>

<style lang="scss">
@import '@/plugins/vuetify/default-preset/preset/pages/auth.scss';

.auth-inner {
    width: 80% !important;
}

.auth-card {
    display: flex;
    flex-direction: column;
}

.auth-inner {
    z-index: 1000 !important;
}

@media (max-width: 500px) {
    .auth-inner {
        width: 100% !important;
    }

}
</style>
