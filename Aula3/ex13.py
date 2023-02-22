def mdc(a,b):
    r = a%b
    if r == 0:
        return b
    return mdc(b,r)

a = int(input("digite o valor de a"))
b = int(input("digite o valor de b"))
print(mdc(a,b))
