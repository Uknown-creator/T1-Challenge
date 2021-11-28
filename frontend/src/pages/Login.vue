<template>
    <div class="auth-wrapper auth-v1">
        <div class="auth-inner">
            <v-card class="auth-card">
                <v-card-text>

                    <v-form>
                        <ScanLarge
                            urlPrefix="/login"
                        />
                    </v-form>
                </v-card-text>
            </v-card>
        </div>
        <v-img
            class="auth-tree"
            width="100%"
            height="100%"
            src="@/assets/images/custom/face-id-login.jpeg"
        ></v-img>
    </div>
</template>

<script>
import ScanLarge from '@/components/ScanLarge'

import { useApi, useCamera, useLoader } from '@/utils'
import {UserModule} from '@/store/questions'

import { ref, watch } from '@vue/composition-api'

export default {
    components: {
        ScanLarge
    },
    setup(props, {root}) {
        const loader = useLoader()

        return {
        }
    },
}
</script>

<style lang="scss">
@import '~@/plugins/vuetify/default-preset/preset/pages/auth.scss';
</style>
