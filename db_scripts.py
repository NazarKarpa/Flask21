import sqlite3

class DataBaseManager:
    def __init__(self, dname):
        self.conn = None
        self.cursor = None
        self.dname = dname


    def open(self):
        self.conn = sqlite3.connect(self.dname)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()



    def get_all_articles(self):
        self.open()
        self.cursor.execute('''SELECT * FROM articles''')
        data = self.cursor.fetchall()
        self.close()
        return data
