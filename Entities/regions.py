import json

class regions:
    def __init__(self,id,nom):
        self.__id = id
        self.__nombre = nom

#getters
    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

#setters
    def setId(self, id):
        self.__id = id
    
    def setNombre(self, nombre):
        self.__nombre = str(nombre)

region1 = regions(1,'La Serena')



