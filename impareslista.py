def encontra_impares(lista):
    if len(lista)<=1:
        if lista[0] % 2 ==0:
            return False
        else:
            return lista[0]
    elif lista[0] % 2 ==1:
        return lista[0],encontra_impares(lista[1:])
    else:
        return encontra_impares(lista[1:])
lista = [1,2,3,4,56,789,9,9,4,989]
print(encontra_impares(lista))