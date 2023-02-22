
def isprime(n):
    cont = n
    primo = 0
    if n == 1:
        return(True)
    else:
        while cont != 0:
            if n%cont == 0:
                primo = primo + 1
            cont -= 1
        if primo == 2:
            return(True)
        else:
            return(False)


n = 0
for i in range(1,101):
    if isprime(i):
        print("o numero {} é primo".format(i))
    else:
        print("o numero {} não é primo".format(i))
