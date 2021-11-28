from db import Database
import random

photo = "bulbulbul"
nick = "artem"
check = Database.if_exist_photo(photo)
if check == "False":
    entities = (nick, random.randint(1, 9999), photo, 0, "null", 0, 0)
    Database.add_user(entities)
res = Database.get_datas_by_photo(photo)
print(res[0][3], res[0][5], res[0][6])