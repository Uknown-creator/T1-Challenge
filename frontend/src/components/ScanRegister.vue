<template>
    <div>
        <v-text-field
            v-model="userName"
            outlined
            required
            label="Имя пользователя"
            placeholder="Иван_Иванов"
            hide-details
            class="mb-3"
        ></v-text-field>
        <div class="main-scan-large">
            <v-img
                src="@/assets/images/custom/face-recognize.png"
                height="150px"
                width="150px"
                class="mb-2"
            />

            <v-alert
                :color="color"
                text
                class="mb-0"
            >
                <div class="d-flex align-start">
                    <v-icon :color="color">
                        {{ icon }}
                    </v-icon>

                    <div class="ms-3">
                        <p class="text-sm font-weight-medium mb-1">
                            {{ text }}
                        </p>
                    </div>
                </div>
            </v-alert>

            <v-btn
                block
                color="success"
                class="mt-6"
                @click="pressRegister"
            >
                Зарегистрироваться
            </v-btn>
        </div>
    </div>
</template>

<script>
import {ref, computed, watch} from "@vue/composition-api"
import {mdiCheckOutline, mdiCloseOutline, mdiAccountClockOutline} from '@mdi/js'
import { useApi, useCamera } from '@/utils'
import { UserModule } from '@/store/questions'
import { testPhoto, initHelpers } from '@/components/scanHelpers'
import {useLoader} from '@/utils'

export default {
    props: {
    },
    setup(props, {root}){
        const userName = ref("");
        const loading = useLoader();

        const {scanSuccessFlag, color, icon, text} = initHelpers(true)

        const {exec, result, error} = useCamera()

        setTimeout(exec, 1000)

        const testData = testPhoto

        const sendDataServer = () => {
            loading.show()
            const request = useApi({
                method: "post",
                url: "/registration",
                data: {
                    nick: userName.value,
                    base64im: result.value
                }
            }, {loading: false})
            request.exec()

            watch(request.result, () => {
                if (request.result.value){
                    scanSuccessFlag.value = 0
                    UserModule.setQuestions(testData)

                    setTimeout(() => {
                        root.$router.push({name: "pages-questions"})
                        loading.hide()
                    }, 2000)
                }
            })

            request.result.value = testData

            // watch(request.error, () => {
            //     scanSuccessFlag.value = 1
            // })
        }

        const pressRegister = () => {
            // not success
            if (!result.value && error.value){
                scanSuccessFlag.value = 1
            }
            // success
            if (result.value){
                setTimeout(sendDataServer, 300)
            }
        }


        return {
            scanSuccessFlag,
            color,
            icon,
            text,
            userName,
            pressRegister
        }
    }
}
</script>

<style>


.main-scan-large {
    display: flex;
    justify-items: center;
    align-items: center;
    flex-direction: column;
}
</style>
