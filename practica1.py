"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
class Rectangulos:
    def area (self, base, altura):
        areaR = base * altura
        return areaR
    
# Crear o instanciar un objeto "rectangulo1" de la clase "Rectangulos"
rectangulo1 = Rectangulos()
print(f"El area del rectangulo es: {rectangulo1.area(5, 6)}")

class Rectangulo: 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
rect = Rectangulo(5, 3)
print(rect.area())

#Implementar el paradigma Orientado a Objetos (OO)
class Rectangulos:
    def area(self, base, altura):
        self.base = base
        self.altura = altura
        
rectangulo1=Rectangulos() #Crear o instanciar objetos "rectangulo1" de la clase "Rectangulos"
print(f"El area del rectangulo es: {rectangulo1.area(5,6)}")