def listatel(n):
    numeros = ['975318642', '234000111', '777888333', '911911911']
    nomes = ['Angelina', 'Brad','Claudia','Bruna']
    if n in numeros:
        for i,word in enumerate(numeros):
            if word == n:
                return(nomes[i])
    else:
        return(n)
            
n = input("Digite um numero")
fim = listatel(n)
print(fim)