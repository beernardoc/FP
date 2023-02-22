import math
def pol(x):
    x1 = int(x)
    p = int(math.pow(x1,2)) + 2*x1 + 3
    return p
    

x = input("Digite o valor de X" + "\n")
print("p(x) = ", pol(x))
