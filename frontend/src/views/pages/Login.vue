<template>
    <div class="auth-wrapper auth-v1">
        <div id="app1" style="display: none"></div>
        <div class="auth-inner">
            <v-card class="auth-card">
                <!-- logo -->
                <v-card-title class="d-flex align-center justify-center py-7">
                    <router-link
                        to="/"
                        class="d-flex align-center"
                    >
                        <v-img
                            :src="require('@/assets/images/custom/face-id-icon.png')"
                            max-height="30px"
                            max-width="30px"
                            alt="logo"
                            contain
                            class="me-3"
                        ></v-img>

                        <h2 class="text-2xl font-weight-semibold">
                            FMProducts
                        </h2>
                    </router-link>
                </v-card-title>

                <v-card-text>
                    <p class="text-2xl font-weight-semibold text--primary mb-2">
                        Face recognition
                    </p>
                    <p class="mb-2">
                        Please sign-in to your account and start the adventure
                    </p>
                </v-card-text>

            </v-card>
        </div>
    </div>
</template>

<script>
import {
    mdiEyeOutline,
    mdiEyeOffOutline,
} from '@mdi/js'


import { useCamera, useLoader } from "@/utils"

import { ref, watch } from '@vue/composition-api'

export default {
    setup() {
        const isPasswordVisible = ref(false)
        const isPinCodeVisible = ref(false)
        const userName = ref('')
        const password = ref('')
        const pinCode = ref('')
        const loader = useLoader()

        watch(userName, () => {
            getScreen()
        })

        const getScreen = () => {
            const {exec} = useCamera()

            exec()
            loader.show()
        }

        return {
            isPasswordVisible,
            isPinCodeVisible,

            userName,
            password,
            pinCode,

            icons: {
                mdiEyeOutline,
                mdiEyeOffOutline,
            },
        }
    },
}
</script>

<style lang="scss">
@import '~@/plugins/vuetify/default-preset/preset/pages/auth.scss';
</style>
