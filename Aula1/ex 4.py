segundos = int(input("Digite os segundos"))
sf = segundos % 60
minutos = int((segundos/60)%60)
horas = segundos//3600
print("{:02d}:{:02d}:{:02d}".format(horas,minutos,sf))



lista = [1,2,3,4]
print(lista[2:5])