<template>
    <v-card class="auth-card">
        <v-card-text>
            <p class="text-xl font-weight-semibold text--primary mb-3">
                {{ header }}
            </p>
            <v-img
                class="question-image"
                :src="src"
            ></v-img>
        </v-card-text>

        <v-card-text>
            <v-form>
                <v-btn
                    block
                    color="primary"
                    class="mt-6"
                    @click="$emit('next_question')"
                >
                    Продолжить ({{ currentNumber + 1 }} из {{ length }})
                </v-btn>
            </v-form>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    props: {
        src: String,
        header: String,
        currentNumber: Number,
        length: Number
    },
    setup(props){
    }
}
</script>

<style lang="scss">
@import '@/plugins/vuetify/default-preset/preset/pages/auth.scss';

.auth-card {
    position: relative;
}

.question-image {
    background-size: cover;
    //min-height: 50%;
    max-height: 70vh;
    //width: 80%;
}

.auth-wrapper.auth-v1 {
    align-items: flex-start !important;
}


</style>
