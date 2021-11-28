import Webcam from 'webcamjs'

Webcam.set({
    width: 1000,
    height: 600,
    image_format: 'jpeg',
    jpeg_quality: 90
})
Webcam.attach("#app")
