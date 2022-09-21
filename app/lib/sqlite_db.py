import sqlite3

from config import DB_NAME

# DB_NAME = 'household_account_book.sqlite3'


class DB():
    def __init__(self, table_name):
        self.table_name = table_name
        self.db_file_path = '../data/' + DB_NAME

        self.connection = sqlite3.connect(self.db_file_path)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def table_isexist(self):
        table_count = self.cursor.execute('''
        SELECT COUNT(*) FROM sqlite_master WHERE TYPE='table' AND name= ?
        ''', (self.table_name,)).fetchone()[0]

        if not table_count == 0:
            return True
        else:
            return False


