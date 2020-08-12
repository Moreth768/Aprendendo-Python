def menor_nome(nomes):
    y=len(nomes[0])
    h=nomes[0].count(' ')
    y=y-h
    curto=str
    a=len(nomes)
    curto=nomes[0]
    for i in range(a):
        z=len(nomes[i])
        h=nomes[i].count(' ')
        z=z-h
        if z<y:
            curto=nomes[i]
        else:
            pass
        y=z
    curto=curto.split()
    nome=curto[0]
    return nome.capitalize()

nomes=['maria', ' josé ', '   PAULO', 'Catarina   ']
print(menor_nome(nomes))