def adj(s):
    j = None
    for i in list(s):
        if i == j:
            s1 = s.replace(j,j,1)
        j = i
    return(s1)

        


s = input("Digite a string")
fim = adj(s)
print(fim)