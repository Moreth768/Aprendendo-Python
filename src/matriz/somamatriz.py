def soma_matrizes(m1, m2):
    m3=[]
    y=len(m1)
    x=len(m1[0])
    y1=len(m2)
    x1=len(m2[0])
    i=j=0
    if y==y1 and x==x1:
        for i in range (y):
            linha = []
            for j in range (x):
                valor = m1[i][j]+m2[i][j]
                linha.append(valor)
            m3.append(linha)
        return m3

    else:
        return False