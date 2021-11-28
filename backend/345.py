from flask import Flask, request
from flask_cors import CORS, cross_origin
from db import Database
import re
from ai import Face
import random
from flask import jsonify
import base64

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/registration", methods=['POST'])
def registration():
    if request.method == 'POST':
        resp = request.get_json()
        photo = resp['base64im']
        nom = str(random.randint(1, 99999)) + "out.jpg"

        with open(nom, "wb") as log:
            splitted = re.sub('data:image/.+;base64,', '', photo)
            print(splitted)
            image_data = base64.b64decode(splitted)
            log.write(image_data)

        m = [i[2] for i in Database.get_users()]
        check = "False"
        for i in m:
            if Face.verify(i[2], nom):
                check = "True"
                break
        if check == "False":
            if 'nick' in resp:
                nick = resp['nick']
            else:
                nick = str(random.randint(1, 9999))
            entities = (nick, random.randint(1, 9999), nom, 0, "null")
            Database.add_user(entities)
        list_of_tests = Database.get_tests()
        res = {
            list_of_tests[0][0]:
                list_of_tests[0][2],
            list_of_tests[1][0]:
                list_of_tests[1][2],
            list_of_tests[2][0]:
                list_of_tests[2][2],
            list_of_tests[3][0]:
                list_of_tests[3][2],
            list_of_tests[4][0]:
                list_of_tests[4][2],
            list_of_tests[5][0]:
                list_of_tests[5][2],
            list_of_tests[6][0]:
                list_of_tests[6][2]
        }
        return jsonify(res)


@app.route("/test", methods=['POST'])
def test():
    if request.method == "POST":
        resp = request.get_json()
        photo = resp['lisBase64im']

        nom = str(random.randint(1, 9999)) + "out.jpg"
        g = open(nom, "w")
        g.write(base64.b64decode(photo[0]))
        g.close()

        m = [i[2] for i in Database.get_users()]
        user_psycho = m[0][4]
        user_d = m[0]
        for i in m:
            if Face.verify(i[2], nom):
                user_d = i
                user_psycho = i[4]
                break
        for i in range(1, 7):
            nom = str(random.randint(1, 9999)) + "out.jpg"
            g = open(nom, "w")
            g.write(base64.b64decode(photo[i]))
            g.close()

            emo = Face.emotion(nom)
            user_psycho = (emo - 3.5) / 2

        res = int(user_psycho)
        Database.add_psychotype(user_d[1], res)

        list_of_photos_goods = Database.get_goods()
        res = {
            list_of_photos_goods[0][1]:
                list_of_photos_goods[0][3],
            list_of_photos_goods[1][1]:
                list_of_photos_goods[1][3],
            list_of_photos_goods[2][1]:
                list_of_photos_goods[2][3],
            list_of_photos_goods[3][1]:
                list_of_photos_goods[3][3],
            list_of_photos_goods[4][1]:
                list_of_photos_goods[4][3],
            list_of_photos_goods[5][1]:
                list_of_photos_goods[5][3]
        }
        return jsonify(res)


@app.route("/goods", methods=['POST'])
def goods():
    if request.method == "POST":
        resp = request.get_json()
        photo = resp['lisBase64im']

        nom = str(random.randint(1, 9999)) + "out.jpg"

        with open(nom, "wb") as log:
            log.write(base64.b64decode(photo[0]))

        m = [i[2] for i in Database.get_users()]
        user_psycho = m[0][4]
        print(user_psycho)
        for i in m:
            if Face.verify(i[2], nom):
                user_psycho = i[4]
                break
        goods_d = Database.get_goods()
        for i in range(6):
            nom = str(random.randint(1, 9999)) + "out.jpg"
            g = open(nom, "w")
            g.write(base64.b64decode(photo[i]))
            g.close()

            emo = Face.emotion(nom)
            goods_sc = m[i][2]
            goods_sc += (emo - 3 + user_psycho) / 2
            Database.add_goods_score(goods_d[i][1], goods_sc)
        return jsonify({"ok": True})


# @app.route("/check_photo", methods=['GET', 'POST'])
# def check_photo():
@app.route("/result_goods")
def result_goods():
    list_of_goods = Database.get_goods()
    res = {
        list_of_goods[0][0]:
            list_of_goods[0][2],
        list_of_goods[1][0]:
            list_of_goods[1][2],
        list_of_goods[2][0]:
            list_of_goods[2][2],
        list_of_goods[3][0]:
            list_of_goods[3][2],
        list_of_goods[4][0]:
            list_of_goods[4][2],
        list_of_goods[5][0]:
            list_of_goods[5][2]
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
