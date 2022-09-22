from lib.sqlite_db import DB


class MainDataModel():
    def __init__(self) -> None:
        self.table_name = 'main'
        self.db = DB(self.table_name)

        isexist = self.db.table_isexist()

        if not isexist:
          self.create_initial_table()

    def create_initial_table(self):
        self.db.cursor.execute('''
        CREATE TABLE main (id INTEGER NOT NULL PRIMARY KEY, date TEXT NOT NULL, item TEXT NOT NULL,category_id INT NOT NULL, price INT NOT NULL)
        ''')
        self.db.connection.commit()

    def create(self, data):
        print(data, 'なぜ')
        self.db.cursor.executemany(
            'INSERT INTO main(date, item, category_id, price) VALUES (?, ?, ?, ?)', data)
        self.db.connection.commit()

    def search_data(self, where):
        data = self.db.cursor.execute(
            f'SELECT * FROM {self.table_name} WHERE date >= ? AND date <= ?', where).fetchall()

        return data

    def delete(self, id):
        self.db.cursor.execute(
            f'DELETE FROM {self.table_name} WHERE id=?', (id,))
        self.db.connection.commit()

    def edit(self, data):
        print(data)
        self.db.cursor.execute(
            f'UPDATE {self.table_name} SET (date, item, category_id, price) = (?, ?, ?, ?) WHERE id=?', data)
        self.db.connection.commit()