def imprime_matriz(matriz):
    y=len(matriz)
    x=len(matriz[0])
    for h in range (y):
        for z in range(x):
            a = matriz[h][z]
            print(a,end=' ')
        print()
    return 

matriz=[[1, 2, 7], [3, 4, 8], [1, 2, 3]]
imprime_matriz(matriz)