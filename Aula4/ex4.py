def fac(n):
    cont = 1
    fac = 1
    while cont <= n:
        fac = fac * cont
        cont = cont + 1
    return(fac)
        
n = int(input("digite o numero N"))
print(fac(n))