<template>
    <div class="auth-wrapper auth-v1">
        <div class="auth-inner">
            <QuestionItem
                @next_question="nextQuestion"
                :src="currentQuestion.src"
                :currentNumber="questionNumber"
                :length="UserModule.products.length"
                header='Посмотрите несколько секунд на товар и нажмите "Продолжить".'
                class="questions-item"
                v-if="!testDone"
            />
            <v-card class="auth-card" v-else>
                <v-card-text>
                    <p class="text-xl font-weight-semibold text--primary mb-3">
                        Спасибо за прохождение опроса!
                    </p>
                </v-card-text>
            </v-card>
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
import { useApi, useCamera, useLoader } from '@/utils'
import {ref, computed, watch} from "@vue/composition-api"
import QuestionItem from "@/components/QuestionItem.vue"
import { UserModule } from '@/store/questions'

export default {
    components: {
        QuestionItem
    },
    setup(){
        const testDone = ref(false)
        const questionNumber = ref(0)
        const resultsData = ref([])
        const loader = useLoader()


        const sendDataToServer = () => {
            loader.show()
            const {exec, result, error} = useApi({
                method: "POST",
                url: "/insert_products",
                data: {
                    listBase64im: resultsData
                }
            }, {"loading": false})
            exec()

            setTimeout(() => {
                loader.hide()
                testDone.value = true
            }, 2000)


        }


        const currentQuestion = computed(() => {
            return UserModule.products[questionNumber.value]
        })

        const savePhoto = () => {
            const {exec, result} = useCamera()
            exec()

            resultsData.value[questionNumber.value] = result.value
        }


        const nextQuestion = () => {
            savePhoto()
            if (questionNumber.value + 1 < UserModule.products.length) {
                questionNumber.value++
            } else {
                sendDataToServer()
            }
        }

        return {
            testDone,
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
