class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def semelhantes(self,t2):
        if (self.a%t2.a)==0 and (self.b%t2.b)==0 and (self.c%t2.c==0):
            return True
        elif (t2.a%self.a)==0 and (t2.b%self.b)==0 and (t2.c%self.c)==0:
            return True
        else:
            return False


t1=Triangulo(2,2,2)
t2=Triangulo(4,4,4)
print(t1.semelhantes(t2))
