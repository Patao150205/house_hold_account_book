from lib.sqlite_db import DB


class RegistDataModel():
    def __init__(self) -> None:
        self.table_name = 'main'
        self.db = DB(self.table_name)

    def create(self, data):
        print(data)
        self.db.cursor.executemany(
            'INSERT INTO main(date, item, price) VALUES (?, ?, ?)', data)
        self.db.connection.commit()
