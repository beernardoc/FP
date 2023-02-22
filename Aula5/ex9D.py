def maiorval(lista):
    j1 = float()
    for i,j in enumerate(lista):
        if j > j1:
            j1 = j
            i1 = i
    return(i1)

lista = [1,2,6,4,5,5]
fim = maiorval(lista)
print(fim)