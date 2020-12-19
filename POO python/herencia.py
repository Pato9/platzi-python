

class Figura():

    def __init__(self,lados,base,altura):
        self.lados = lados
        self.base = base
        self.altura = altura

class Cuadrado(Figura):

    def __init__(self,lados, base, altura):
        super().__init__(lados, base, altura)

    def validar_cuadrado(self):
        if self.base == self.altura:
            return True
        else:
            return False

    def area(self):
        a = self.base * self.altura
        return a

class Triangulo(Figura):

    def __init__(self,lados,base,altura):
        super().__init__(lados,base,altura)

    def validar_triangulo(self):
        if self.lados == 3:
            return True
        else:
            return False

    def area(self):
        a = (self.base*self.altura)/2
        return a

class Rectangulo(Cuadrado):

    def __init__(self,lados,base,altura):
        super().__init__(lados,base,altura)


    def validar_rectangulo(self):
        if self.lados == 4:
            return True
        else:
            return False



if __name__ == '__main__':
    mi_cuadrado = Cuadrado(lados=4,base=4,altura=4)
    mi_triangulo = Triangulo(lados=4,base=13,altura=16)
    mi_rectangulo = Rectangulo(lados=4,base=15,altura=10)

    print(mi_cuadrado.validar_cuadrado())
    print(f'El area del cuadrado es : {mi_cuadrado.area()}')
    print(f'El area del triangulo es :{mi_triangulo.area()}')
    print(f'El area del rectangulo es :  {mi_rectangulo.area()}')




