class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return (self.a+self.b+self.c)


if __name__ == "__main__":
    a = Triangulo(1,23,5)

    print(a.perimetro())
