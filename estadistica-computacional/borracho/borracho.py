import random

class Borracho():

    def __init__(self,nombre):
        self.nombre = nombre


    def movimiento(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0),(3,0),(0,3),(-3,0),(0,-3)])


