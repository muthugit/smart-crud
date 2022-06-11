import abc

class BaseEngine(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_table(self, tbl_schema: dict):
        print("Hi---")
        return