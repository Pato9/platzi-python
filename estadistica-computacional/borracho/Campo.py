
class Campo():

    def __init__(self):
        self.coordenada_borracho = {}

    
    def anadir_borracho(self,borracho,coordenada):
        self.coordenada_borracho[borracho] = coordenada

    def mover_borracho(self,borracho):
        delta_x,delta_y = borracho.camina()

        coordenada_actual = self.coordenada_borracho[borracho]

        nueva_coordenada = coordenada_actual.mover(delta_x,delta_y)

        self.coordenada_borracho[borracho] = nueva_coordenada
    
    def obtener_coordenada(self,borracho):
        return self.coordenada_borracho[borracho]
    

    