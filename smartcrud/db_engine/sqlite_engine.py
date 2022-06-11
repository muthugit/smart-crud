from typing import overload
import sqlalchemy
from smartcrud.db_engine import BaseEngine

class SQLite(BaseEngine):
    def __init__(self, connection: dict) -> None:
        super(BaseEngine, self).__init__()
        self.engine=sqlalchemy.create_engine(f"sqlite:///{connection['path']}/{connection['db_name']}")

    @staticmethod
    def get_dtype(type_name):
        if type_name == "str":
            return "TEXT"
        elif type_name in ["int", "float"]:
            return "INTEGER"

    def create_table(self, tbl_schema: dict):
        print("Hi")
        cols = []
        cols.append(f"{tbl_schema['tbl_name']}_id INTEGER PRIMARY KEY")
        for col in tbl_schema['cols']:
            null_ck = "NULL"
            if col in tbl_schema['required']:
                null_ck = "NOT NULL"
            cols.append(f"{col} {self.get_dtype(tbl_schema['cols'][col])} {null_ck}")
        
        query = f"""
                CREATE TABLE if not exists {tbl_schema['tbl_name']} (
                    {",".join(cols)}
                );
                """
        self.engine.execute(query)

        

if __name__ == "__main__":
    connection = {
        "path": "/opt/muthu/smart-crud/example_app/",
        "db_name": "mydb.db"
    }
    schema = {
     "tbl_name": "temp",
     "cols": {
        "name": "str",
        "price": "int",
         "is_active": "bool",
         "tag": "str",
         "godown_id": "int"
     },
     "required": ['name', 'price', 'tag']
    }
    sq = SQLite(connection=connection)
    sq.create_tbl(schema)