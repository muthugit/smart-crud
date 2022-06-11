import abc
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, Float

class BaseEngine(metaclass=abc.ABCMeta):
    def __init__(self):
        self.engine = None
        self.dtypes = {
            "str": String,
            "int": Integer,
            "float": Float,
            "bool": Boolean
        }
        self.models = {}

    def get_dtype(self, type_name):
        return self.dtypes[type_name]

    def load_models(self, repo_dir):
        pass

    def create_model(self, tbl_schema):
        meta = MetaData()
        tbl = Table(
            tbl_schema['tbl_name'], meta
            )
        p_col = Column(f"{tbl_schema['tbl_name']}_id", Integer, primary_key=True)
        tbl.append_column(p_col)
        for col in tbl_schema['cols']:
            nullable = True
            if col in tbl_schema['required']:
                nullable = False
            print(f"{col} => Required: {nullable}")
            column = Column(col, self.get_dtype(tbl_schema['cols'][col]), nullable=nullable)
            tbl.append_column(column)
        meta.create_all(self.engine)

    def select(self, tbl_name):
        sql = f'select * from {tbl_name}'
        result = self.engine.execute(sql).fetchall()
        data = [dict(row) for row in result]
        return data
        