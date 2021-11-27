import sqlite3

con = sqlite3.connect('database.db', check_same_thread=False)
cursorObj = con.cursor()


class Database:
    def if_exist_photo(photo):
        check = cursorObj.execute("SELECT * FROM users WHERE photo_path=?", (photo, ))
        z = check.fetchall()
        print(z)
        if len(z) == 0:
            return "False"
        else:
            return "True"

    def add_user(entities):
        cursorObj.execute(f"INSERT INTO users VALUES(?, ?, ?, ?, ?)", entities)

        # nickname, id, photo_path, admin, psychotype

        con.commit()

    def get_users():
        cursorObj.execute("SELECT * FROM users")
        return cursorObj.fetchall()

    def Admin(id, isAdmin):
        cursorObj.execute(f"UPDATE users SET admin = '{isAdmin}' WHERE id = {id}")
        con.commit()

    def delete_user(id):
        cursorObj.execute(f"DELETE FROM users WHERE id = '{id}'")
        con.commit()

    def add_psychotype(id, psychotype):
        cursorObj.execute(f"UPDATE users SET psychotype = '{psychotype}' WHERE id = {id}")
        con.commit()

    def add_goods(entities):
        cursorObj.execute(f"INSERT INTO goods VALUES(?, ?, ?, ?)", entities)

        # name, id, score, photo_path
        con.commit()

    def delete_goods(id):
        cursorObj.execute(f"DELETE FROM goods WHERE id = '{id}'")
        con.commit()

    def add_goods_score(id, score):
        cursorObj.execute(f"UPDATE goods SET score = '{score}' WHERE id = {id}")
        con.commit()

    def get_goods():
        cursorObj.execute("SELECT * FROM goods")
        return cursorObj.fetchall()
