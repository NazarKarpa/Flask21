import sqlite3

class DataBaseManager:
    def __init__(self, dname):
        self.conn = sqlite3.connect(dname)
        self.cursor = self.conn.cursor()

    def get_all_articles(self):
        self.cursor.execute('''SELECT * FROM articles''')
        data = self.cursor.fetchall()
        return data
