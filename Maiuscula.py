def maiusculas(frase):
    h=len(frase)
    curto=""
    for i in range (h):
        tabela=ord(frase[i])
        if tabela>=65 and tabela<=90:
            curto = curto + frase[i]
        else:
            pass
    return curto
frase='Programamos em python 2?'
print(maiusculas(frase))