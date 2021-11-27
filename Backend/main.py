from flask import Flask
from db import Database
import random

# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
#
# if __name__ == "__main__":
#     app.run()
photo = "C:/users/sfsdi/sjs"

datas = ("Забор Артёмщиков", random.randint(1, 99), 0.7, "C:/porn/artem/gay.png")

Database.add_goods_score("null", 80, -0.5)
