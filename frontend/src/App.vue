<template>
    <v-app>
        <nav class="app-navigation-menu v-navigation-drawer v-navigation-drawer--fixed v-navigation-drawer--floating v-navigation-drawer--open"
             data-booted="true"
             style="height: 100vh; top: 0px; transform: translateX(0%); width: 260px; max-height: calc(100% - 0px);"
        >
            <div class="v-navigation-drawer__content">
                <div class="vertical-nav-header d-flex items-center ps-6 pe-5 pt-5 pb-2">
                    <a href="/" class="d-flex align-center text-decoration-none router-link-active"
                >
                    <v-img
                        :src="require('@/assets/images/custom/logo.png')"
                        max-height="70px"
                        max-width="70px"
                        alt="logo"
                        contain
                        eager
                        class="app-logo me-3"
                    ></v-img>
                    <h1 class="app-title text--primary"> FMProducts </h1>
                    </a>
                </div>
            </div>
        </nav>
        <v-main>
            <loader object="#ff9633" color1="#ffffff" color2="#17fd3d" size="5" speed="2" bg="#343a40"
                    objectbg="#999793" style="z-index: 4000 !important; position: fixed"
                    opacity="80" name="circular" v-if="isLoading"
            ></loader>
            <router-view style="z-index: 1100"></router-view>
        </v-main>
    </v-app>
</template>

<script>
import { computed } from '@vue/composition-api'
import { useRouter, isLoading } from '@/utils'
import LayoutBlank from '@/layouts/Blank.vue'
import LayoutContent from '@/layouts/Content.vue'

export default {
    components: {
        LayoutBlank,
        LayoutContent,
    },
    setup() {
        return {
            isLoading,
        }
    },
}
</script>
