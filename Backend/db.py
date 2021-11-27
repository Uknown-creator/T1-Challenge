import sqlite3

con = sqlite3.connect('database.db')

cursorObj = con.cursor()


class Database:
    def add_user(self, entities):
        cursorObj.execute(f"INSERT INTO users VALUES(?, ?, ?, ?)", entities)

        # nickname, id, photo_path, admin
        con.commit()

    def Admin(self, id, isAdmin):
        cursorObj.execute(f"UPDATE users SET admin = '{isAdmin}' WHERE id = {id}")
        con.commit()

    def delete_user(self, id):
        cursorObj.execute(f"DELETE FROM users WHERE id = '{id}'")
        con.commit()

    def add_goods(self, entities):
        cursorObj.execute(f"INSERT INTO goods VALUES(?, ?, ?, ?)", entities)

        # name, id, score, photo_path
        con.commit()

    def delete_goods(self, id):
        cursorObj.execute(f"DELETE FROM goods WHERE id = '{id}'")
        con.commit()

    def add_goods_score(self, id, score):
        cursorObj.execute(f"UPDATE goods SET score = '{score}' WHERE id = {id}")
        con.commit()
