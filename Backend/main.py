from flask import Flask
from db import Database
import random
import json
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    return "Hell. World!"


@app.route("/add_user", methods=['GET', 'POST'])
def users():
    # handle the POST request
    if request.method == 'POST':
        nick = request.form.get('nick')
        photo = request.form.get('photo')
        datas = (nick, random.randint(1, 99), photo, 0, "null")
        Database.add_user(datas)
        return "Data received, check bd"

    # otherwise handle the GET request
    return '''
               <form method="POST">
                   <div><label>Nick: <input type="text" name="nick"></label></div>
                   <div><label>Photo: <input type="text" name="photo"></label></div>
                   <input type="submit" value="Submit">
               </form>'''


@app.route("/goods")
def goods():
    return str(Database.get_goods())


@app.route("/check_photo", methods=['GET', 'POST'])
def check_photo():
    if request.method == 'POST':
        photo = request.form.get('photo')
        check = Database.if_exist_photo(photo)
        return check
    return '''
                <form method="POST">
                    <div><label>Photo: <input type="text" name="photo"></label></div>
                    <input type="submit" value="Submit">
                </form>'''


if __name__ == "__main__":
    app.run()
# photo = "C:/users/sfsdi/sjs"
#
# datas = ("Забор Артёмщиков", random.randint(1, 99), 0.7, "C:/porn/artem/gay.png")
#
# Database.add_psychotype("null", 31, "positive")
