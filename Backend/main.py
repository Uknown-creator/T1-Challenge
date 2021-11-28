from flask import Flask, request
from db import Database
import random
import jsonify

app = Flask(__name__)


@app.route("/")
@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        resp = request.json
        photo = resp['photo']
        nick = resp['nick']
        check = Database.if_exist_photo(photo)
        if check == "False":
            entities = (nick, random.randint(1, 9999), photo, 0, "null")
            Database.add_user(entities)
        res = Database.get_datas_by_photo(photo)
        req = {
            "Admin": res[0][3],
            "Test": res[0][5],
            "Goods": res[0][6]
        }
        return jsonify(req)
    return '''
                <form method="POST">
                    <div><label>Photo: <input type="text" name="photo"></label></div>
                    <input type="submit" value="Submit">
                </form>'''


@app.route("/test", methods=['GET', 'POST'])
def test():
    if request.method == "POST":
        resp = request.json
        photo = resp['photo']
        id_test = resp['id_test']

        user_d = Database.get_datas_by_photo(photo)
        user_psycho = user_d[0][4]
        test_d = Database.get_score_by_test(id_test)
        test_score = test_d[0][1]
        res = int(user_psycho) + int(test_score)
        Database.add_psychotype(user_d[0][1], res)
        return {
            "ok": True
        }
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


@app.route("/goods", methods=['GET', 'POST'])
def goods():
    if request.method == "POST":
        resp = request.json
        photo = resp['photo']
        id_goods = resp['id_goods']

        user_d = Database.get_datas_by_photo(photo)
        user_psycho = user_d[0][4]
        goods_d = Database.get_score_by_goods(id_goods)
        test_score = goods_d[0][2]
        res = int(user_psycho) + int(test_score)
        Database.add_goods_score(id_goods, res)
        return jsonify({
            "ok": True
        })
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
    app.run()
