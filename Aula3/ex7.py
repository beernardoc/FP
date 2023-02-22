def tax(r):

    if r <= 1000:
        res = float(0.1*r)
    elif r > 1000 and r <=2000:
        res = float((0.2*r) - 100)
    else:
        res = float((0.3*r) - 300)
        
    return(res)

r = int(input("Digite o valor de R"))
print("O resultado é:", tax(r))
