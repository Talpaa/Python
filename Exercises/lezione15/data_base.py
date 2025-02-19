class DatabaseConnection:

    def __init__(self, db_name: str) -> None:
        
        self.db_name = db_name
        self.connection = None

    def connect(self):

        print(f'Connecting to database: {self.db_name}')

        self.connection = f'Connection to {self.db_name}'

    def disconnect(self):

        print(f'Disconnecting to database: {self.db_name}')

        self.connection = None

    def commit(self):
        print(f'Committing transaction')

    def rollback(self):
        print(f'Rolling back transaction')

    def execute_query(self, query): # type: ignore

        print(f'Executing query: {query}')

        return f'Results of \'{query}\''