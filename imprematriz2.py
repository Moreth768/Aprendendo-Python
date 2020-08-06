def imprime_matriz(minha_matriz):
    	
	line = len(minha_matriz)
	colunm = len(minha_matriz[0])

	for i in range(line):
		for j in range(colunm):
			
			if (j != (colunm-1)) :
				print(minha_matriz[i][j],end=' ')
			else : 
				print(minha_matriz[i][j])

matriz=[[1, 2, 7], [3, 4, 8], [1, 2, 3]]
imprime_matriz(matriz)