def inter(a1,b1,a2,b2):
    lista =[]
    lista1 = []
    inter = 0
    while not a1 > b1:
        lista.append(a1)
        a1 = a1 + 0.1
    while not a2 > b2:
        lista1.append(a2)
        a2 = a2 + 0.1
    for i in lista:
        for j in lista1:
            if i == j:
                inter = inter + 1
    if inter == 0:
        return(False)
    else:
        return(True)

a1 = int(input("Digite o valo de A1"))
b1 = int(input("Digite o valo de B1"))
a2 = int(input("Digite o valo de A2"))
b2 = int(input("Digite o valo de B2"))
if a1 <= b1 and a2 <=b2:
    print(inter(a1,b1,a2,b2))
else:
    print("ERRO")
