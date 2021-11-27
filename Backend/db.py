import sqlite3

con = sqlite3.connect('database.db')

cursorObj = con.cursor()


class Database:
    def add_user(self, entities):
        cursorObj.execute(f"INSERT INTO users VALUES(?, ?, ?, ?)", entities)

        con.commit()

    def add_photo(self, entities):
        cursorObj.execute(f"INSERT INTO photos VALUES(?, ?)", entities)
        con.commit()


    def delete_user(self, id):
        cursorObj.execute(f"DELETE FROM users WHERE id = '{id}'")
        con.commit()
    def delete_photo(self, id):
        cursorObj.execute(f"DELETE FROM photos WHERE id = '{id}'")
        con.commit()