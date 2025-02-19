#from abc import ABC, abstractmethod

class Film():

    def __init__(self, id: int, title: str) -> None:
        
        self.__id = id
        self.title = title

    def setID(self, id: int):

        self.__id = id

    def setTitle(self, title: str):

        self.title = title

    def getID(self):

        return self.__id
    
    def getTitle (self):

        return self.title
    
    def isEqual(self, other_film: 'Film'):

        if self.getID() == other_film.getID:

            return True
        
        else:

            return False
        
    ''' @abstractmethod    
    def calcolaPenaleRitardo():

        pass'''