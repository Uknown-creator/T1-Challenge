<template>
    <div class="auth-wrapper auth-v1">
        <div class="auth-inner">
            <v-card class="auth-card">
                <v-card-text>
                    <p class="text-2xl font-weight-semibold text--primary mb-2">
                        Распознавание лиц
                    </p>
                    <p class="mb-2">
                        Заполните форму и отсканируйте свое лицо.
                    </p>
                </v-card-text>

                <v-card-text>
                    <v-form>

                        <ScanRegister />

                        <v-btn
                            block
                            color="primary"
                            class="mt-6"
                            @click="$router.push({'name': 'pages-login'})"
                        >
                            Войти по FACE ID
                        </v-btn>
                    </v-form>
                </v-card-text>

            </v-card>
        </div>
        <v-img
            class="auth-tree"
            width="100%"
            height="100%"
            src="@/assets/images/custom/face-id-background.png"
        ></v-img>
    </div>
</template>

<script>
import {
    mdiEyeOutline,
    mdiEyeOffOutline,
} from '@mdi/js'

import { useCamera, useLoader } from "@/utils"

import { ref, watch } from '@vue/composition-api'
import ScanRegister from '@/components/ScanRegister'

export default {
    components: {
        ScanRegister,
    },
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
