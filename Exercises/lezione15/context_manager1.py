from typing import Any

class FileManager:

    def __init__(self, file_name: str, mode: str) -> None:
        
        self.file_name: str = file_name
        self.mode: str = mode

    
    def __enter__(self):

        self.file_wrapper = open(self.file_name, self.mode)

        return self.file_wrapper
    
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any):

        self.file_wrapper.close()


with FileManager(file_name='prova.txt', mode='w') as file:

    file.write('Ciao')