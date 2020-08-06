class Triangulo:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.perimetro()
        return
    def perimetro(self):
        self.perimetro=self.a+self.b+self.c
        return self.perimetro
