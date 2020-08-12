import random
def lista_grande(n):
    lista=[]
    for i in range (n):
        lista.append(random.randrange(1000))
    return lista
lista=[1,2,3,5,4]
x=len(lista)