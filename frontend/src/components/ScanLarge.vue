<template>
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
    </div>
</template>

<script>
import {ref, computed, watch} from "@vue/composition-api"
import {mdiCheckOutline, mdiCloseOutline, mdiAccountClockOutline} from '@mdi/js'
import { useApi, useCamera } from '@/utils'
import { UserModule } from '@/store/questions'
import { testPhoto, initHelpers } from '@/components/scanHelpers'

export default {
    props: {
        urlPrefix: String,
    },
    setup(props, {emit, root}){
        const {scanSuccessFlag, color, icon, text} = initHelpers()

        const {exec, result, error} = useCamera()

        const testData = testPhoto

        setTimeout(exec, 1000)

        const sendDataServer = () => {
            const request = useApi({
                method: "POST",
                url: props.urlPrefix,
                data: {base64im: result.value}
            }, {loading: false})
            request.exec()

            watch(request.result, () => {
                if (request.result.value){
                    scanSuccessFlag.value = 0
                    UserModule.setQuestions(testData)

                    setTimeout(() => {
                        root.$router.push({name: "pages-questions"})
                    }, 2000)
                }
            })

            request.result.value = testData

            // watch(request.error, () => {
            //     scanSuccessFlag.value = 1
            // })
        }

        watch(result, () => {
            // not success
            if (!result.value && error.value){
                scanSuccessFlag.value = 1
            }
            // success
            if (result.value){
                setTimeout(sendDataServer, 300)
            }
        })


        return {
            scanSuccessFlag,
            color,
            icon,
            text
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
