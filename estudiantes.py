print("\033c")

class Estudiantes:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    @property
    def nombre (self):
        return self._nombre
    
    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre
        
    @property
    def nota (self):
        return self._nota
    
    @nota.setter
    def nota (self, nota):
        self._nota = nota