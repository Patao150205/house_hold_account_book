from lib.sqlite_db import DB
import os


class CategoryDataModel():
    def __init__(self) -> None:
        self.table_name = 'category'
        self.db = DB(self.table_name)

        isexist = self.db.table_isexist()

        if not isexist:
            self.create_initial_table()

    def get_categories_from_file(self):
        basedir =  os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(basedir, '../data/category.txt')

        print(path)
        with open(path, mode='r') as f:
            categories =  f.read().splitlines()
            
        return categories

    def create_initial_table(self):
        categories = self.get_categories_from_file()

        self.db.cursor.execute(f'''
        CREATE TABLE {self.table_name} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name text NOT NULL)
        ''')

        for category in categories:
            self.db.cursor.execute(f'''
                INSERT INTO {self.table_name} (name) VALUES (?)
            ''', (category,))

        self.db.connection.commit()

    def get(self):
        data = self.db.cursor.execute(f'''
        SELECT * FROM {self.table_name}
        ''')
        
        categories = data.fetchall()

        return categories