class SerVivo:

    def dormir(self):
        print('El ser duerme.')

class Animal(SerVivo): # Clase Padre
    
    def comer(self):
        print('El animal come.')

class Mascota(Animal): # Clase Padre
    
    def comer(self):
        super().comer()
        print(type(super()))
        print('La mascota come.')

class Felino:

    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino): # Clase Hija
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.nombre} come.')


patricio = Gato('Patricio')

patricio.comer()
