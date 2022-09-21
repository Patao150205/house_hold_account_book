import sqlite3

from config import DB_NAME

# DB_NAME = 'household_account_book.sqlite3'


class DB():
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_file_path = '../data/' + DB_NAME

        self.connection = sqlite3.connect(self.db_file_path)
        self.cursor = self.connection.cursor()
        isexist = self.table_isexist()

        if isexist:
            pass
        else:
            self.create_initial_table()

    def __del__(self):
        self.connection.close()

    def send_query_to_db(self, func):
        pass

    def table_isexist(self):
        table_count = self.cursor.execute('''
        SELECT COUNT(*) FROM sqlite_master WHERE TYPE='table' AND name= ?
        ''', (self.table_name,)).fetchone()[0]

        if not table_count == 0:
            return True
        else:
            return False

    def create_initial_table(self):
        self.cursor.execute('''
        CREATE TABLE main (id INTEGER NOT NULL PRIMARY KEY, date TEXT NOT NULL, item TEXT NOT NULL, price INT NOT NULL)
        ''')
        self.connection.commit()
