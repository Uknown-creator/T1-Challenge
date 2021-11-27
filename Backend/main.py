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
datas = ("Kuskov", "Maxim", "Alexandrovich", random.randint(1, 96))
photo = ("C:/users/sfsdi/sjs", 91)

Database.delete_photo("NULL", 91)
