import sqlalchemy
from smartcrud.db_engine import BaseEngine


class SQLite(BaseEngine):
    def __init__(self, connection: dict) -> None:
        super().__init__()
        self.engine=sqlalchemy.create_engine(f"sqlite:///{connection['path']}/{connection['db_name']}")


if __name__ == "__main__":
    connection = {
        "path": "/opt/muthu/smart-crud/example_app/",
        "db_name": "mydb.db"
    }
    schema = {
     "tbl_name": "dynamic212",
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
    # sq.create_tbl(schema)
    sq.create_model(schema)