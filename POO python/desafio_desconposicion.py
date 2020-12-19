

class Auto():

    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self._velocidad_tope = 230
        self._motor = Motor(cilindros=4) 


    def en_movimiento(self,velocidad_inicial):
        gasolina = 20
        for i in range(velocidad_inicial,self._velocidad_tope+1):
        
            if i == self._velocidad_tope:
                print('sin gasolina... ')
                gasolina = int(input('Ingresa total de gasolina\n >'))

                self._motor.inyecta_gasolina(gasolina)
    
    def cambio_color(self):
        new_color = input('Ingrese nuevo color \n>')
        self.color = new_color

    def distancia(self,velocidad,tiempo):
        d = velocidad*tiempo 
        return d
    
    def tiempo(self,velocidad,distancia):
        t = distancia/velocidad
        return t

    

class Motor():

    def __init__(self,cilindros,tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        
    def inyecta_gasolina(self, gasolina):
        print(f'usted ha colocado {gasolina} litros')

mi_auto = Auto('Nissan','GTR-35','Azul')
mi_auto.en_movimiento(0)
mi_auto.cambio_color()
print(mi_auto.tiempo(120,1000))



print(mi_auto.color)



