import { computed, ref } from '@vue/composition-api'
import { mdiAccountClockOutline, mdiCheckOutline, mdiCloseOutline } from '@mdi/js'


export const testPhoto = [
    {
        src: require("@/assets/images/tests/FgkBZIbvk54.jpg")
    },
    {
        src: require("@/assets/images/tests/FS3kI-_yfvs.jpg")
    },
    {
        src: require("@/assets/images/tests/HfAvf04TJZ0.jpg")
    },
    {
        src: require("@/assets/images/tests/L9M-zuHNQrk.jpg")
    },
    {
        src: require("@/assets/images/tests/lxw18PKwf6o.jpg")
    },
    {
        src: require("@/assets/images/tests/MRM6I9J6jOw.jpg")
    },
    {
        src: require("@/assets/images/tests/nh-OpvU6FAI.jpg")
    }
]


export const prodPhoto = [
    {
        src: require("@/assets/images/prod/AMf3BtwqM7Y.jpg")
    },
    {
        src: require("@/assets/images/prod/HzFnYdA9XeI.jpg")
    },
    {
        src: require("@/assets/images/prod/MumRnScvf5s.jpg")
    },
    {
        src: require("@/assets/images/prod/nS1WVHfbDGw.jpg")
    },
    {
        src: require("@/assets/images/prod/Opera_Snimok_2021-11-28_142018_aliexpress_ru.png")
    },
    {
        src: require("@/assets/images/prod/Opera_Snimok_2021-11-28_142037_aliexpress_ru.png")
    }
]



export const initHelpers = (isRegister=false) => {
    // 0 - success, 1 - error, -1 - not started
    const scanSuccessFlag = ref(-1)

    const color = computed(() => {
        if (scanSuccessFlag.value === 1){
            return "warning"
        } else if (scanSuccessFlag.value === 0){
            return "success"
        } else if (scanSuccessFlag.value === -1){
            return "gray"
        }
    })

    const icon = computed(() => {
        if (scanSuccessFlag.value === 1){
            return mdiCloseOutline
        } else if (scanSuccessFlag.value === 0){
            return mdiCheckOutline
        } else if (scanSuccessFlag.value === -1) {
            return mdiAccountClockOutline
        }
    })

    const text = computed(() => {
        if (scanSuccessFlag.value === 1){
            return "Ошибка во время сканирования!"
        } else if (scanSuccessFlag.value === 0){
            return "Успешное сканирование лица!"
        } else if (scanSuccessFlag.value === -1){
            if (isRegister){
                return "Нажмите на кнопку..."
            }
            return "Выполняется сканирование..."
        }
    })

    return {scanSuccessFlag, color, icon, text}
}
