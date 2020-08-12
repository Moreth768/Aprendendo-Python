def ordenada(lista):
    x=lista[0]
    for i in range(1,len(lista)):
        if x>=lista[i]:
            return False
        x=lista[i]
    return True

