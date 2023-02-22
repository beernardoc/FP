def inputfloatlist():
   lista = []
   n = input("Digite um valor")
   while n != '':
       if n == '':
           break
       else:
           lista.append(n)
           n = input("Digite um valor")
   return(lista)

       


fim = inputfloatlist()
print(fim)

