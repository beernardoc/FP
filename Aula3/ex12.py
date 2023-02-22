def countdown(n):
    cont = 0
    while not cont == n:
        print(n - cont)
        cont = cont + 1

n = int(input("Digite o valor de N"))
countdown(n)n