// eslint-disable-next-line object-curly-newline
import axios from 'axios'
import Webcam from "webcamjs"
import { getCurrentInstance, reactive, toRefs, watch, ref } from '@vue/composition-api'


export const isLoading = ref(false)


export const useRouter = () => {
    const vm = getCurrentInstance().proxy

    const state = reactive({
        route: vm.$route,
    })

    watch(
        () => vm.$route,
        r => {
            state.route = r
        },
    )

    return {
        ...toRefs(state),
        router: vm.$router,
    }
}


export function useCamera(){
    const result = ref(null)
    const error = ref(null)

    const exec = () => {
        Webcam.snap(
            function (data){
                result.value = data
                error.value = true
            }
        )
    }
    return {exec, result, error}
}


export function useApi(
    request,
    options={loading: true},
    handleResponse = async (data) => data.data,
) {
    // const baseURL = process.env.NODE_ENV === 'production' ? 'https://chat.ucabix.com/api/v1' : 'http://localhost:5000/v1'
    // const baseURL = "http://10.70.5.25:5000/"
    const baseURL = "http://localhost:5005"
    const $axios = axios.create({
        baseURL,
        withCredentials: true,
        maxRedirects: 0,
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            'content-type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    })

    // $axios.interceptors.request.use((config) => {
    //     // const token = UserModule.token
    //     //
    //     // if (token) {
    //     //     config.headers.Authorization = `Bearer ${token}`
    //     // }
    //     //
    //     // return config
    // })
    const result = ref(null)
    const error = ref(null)
    const exec = async () => {
        if (options?.loading){
            isLoading.value = true
        }

        error.value = null
        try {
            const response = await $axios(request)
            const valueResponse = await handleResponse(response)
            result.value = valueResponse
            return valueResponse
        } catch (e) {
            if (e.isAxiosError) {
                error.value = e
                console.log('error', e)
            } else {
                console.log('strange error ', e)
                error.value = e
            }
            result.value = null
        } finally {
            if (options?.loading){
                isLoading.value = false
            }
        }
    }

    return {
        exec,
        result,
        error,
    }
}



export function useLoader(){
    const show = () => {
        isLoading.value = true
    }

    const hide = () => {
        isLoading.value = false
    }

    return {show, hide}
}

