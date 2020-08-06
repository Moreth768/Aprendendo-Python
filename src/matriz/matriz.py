def cria_matriz (matriz,num_linhas,num_colunas):
    for i in range (num_linhas):
        linha = []
        for j in range (num_colunas):
            valor=int(input('Digite o valor:'))
            linha.append(valor)
        matriz.append(linha)
    return matriz
def matriz_correta (num_linhas,num_colunas,m1):
    for h in range (num_linhas):
        for z in range(num_colunas):
            x = m1[h][z]
            print(x,end=' ')
        print()
    return (num_linhas,num_colunas,matriz)


num_linhas=int(input('Digite o numero de linhas:'))
num_colunas=int(input('Digite o numero de colunas:'))
matriz=[]
(cria_matriz(matriz,num_linhas,num_colunas))
(matriz_correta(num_linhas,num_colunas,matriz))