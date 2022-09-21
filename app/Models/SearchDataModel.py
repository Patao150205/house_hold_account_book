from lib.sqlite_db import DB


class SearchDataModel():
    def __init__(self) -> None:
        self.table_name = 'main'
        self.db = DB(self.table_name)

    def search_data(self):
        data = self.db.cursor.execute(
            f'SELECT * FROM {self.table_name}').fetchall()

        return data
