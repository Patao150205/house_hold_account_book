from lib.sqlite_db import DB


class EditSearchDataModel():
    def __init__(self) -> None:
        self.table_name = 'main'
        self.db = DB(self.table_name)

    def delete(self, id):
        print(id, 'ぱたお')
        self.db.cursor.execute(
            f'DELETE FROM {self.table_name} WHERE id=?', (id,))
        self.db.connection.commit()

    def edit(self, data):
        print(data)
        self.db.cursor.execute(
            f'UPDATE {self.table_name} SET (date, item, price) = (?, ?, ?) WHERE id=?', data)
        self.db.connection.commit()
