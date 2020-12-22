class Coordenada():

    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def mover(self,delta_x,delta_y):
        return Coordenada(delta_x+self.x,delta_y+self.y)

    def distancia(self,otra_cordenada):
        delta_x = self.x - otra_cordenada.x
        delta_y = self.y - otra_cordenada.y 

        return (delta_x**2+delta_y**2)**0.5