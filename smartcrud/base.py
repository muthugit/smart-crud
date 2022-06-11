import json
from smartcrud.db_engine import BaseEngine
from smartcrud.db_engine import SQLite


class SmartCrud:
    def __init__(self, repository_dir) -> None:
        self.db_engine:BaseEngine = None
        self.repository = repository_dir
        

    @property
    def repository(self):
        return self._repository

    @repository.setter
    def repository(self, value):
        data = None
        with open(f"{value}/db.json", 'r') as f:
            data = json.load(f)
        print(data['db_type'])
        if data['db_type'] == "SQLite":
            print("Setting SQLite")
            self.db_engine = SQLite(data['connection'])
        self._repository = data

    def create_table(self, schema: dict):
        self.db_engine.create_table(schema)