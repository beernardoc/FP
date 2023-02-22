def maiusc(s):
    i1 = str("")
    for i in list(s):
        j = i.isupper()
        if j == True:
            i1 = i1 + i
    return(i1)
s = input("Digite um nome")
fim = maiusc(s)
print(fim)
