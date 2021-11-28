from deepface import DeepFace as deepf


class Face:
    def verify(img, img2):
        '''
        Сравнение лица с другим. На вход подаётся путь к изображению лица
        '''
        res = deepf.verify(img1_path=img, img2_path=img2, model_name='VGG-Face')
        return res['verified']

    def emotion(img):
        '''
        Определение эмоции
        '''

        res = deepf.analyze(img, actions=['emotion'])
        m = res['emotion']
        resul = m["neutral"]
        k = 7
        con = 0
        print(m)
        for i in m:
            con += 1
            if m[i] > resul:
                resul = m[i]
                k = con
        return k


    def whois(img):
        '''
        Определение возраста, пола и рассы
        '''
        res = deepf.analyze(img, actions=['age', 'gender', 'race'])
        m = res['race']
        resul = m["white"]
        z = "white"
        for i in m:
            if m[i] > resul:
                resul = m[i]
                z = i
        return {'age': res['age'],
                'gender': res['gender'],
                'race': z}
