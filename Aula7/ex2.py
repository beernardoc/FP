def addContact(contactos):
    nome = input("digite o nome")
    numero = input("digite o numero")
    contactos[numero] = nome
    return contactos

def delContact(numero,contactos):
    del contactos[numero]
    return contactos

def proContact(num,contactos):
    print(contactos.get(num, num))
    


def menu():
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op

def filterPartName(contactos, partName):
    for num,name in contactos.items():
        if partName in name:
            print(num,name)
            
    




def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
           addContact(contactos)
           listContacts(contactos)
        elif op == "R":
            numero = input("digite o numero que quer remover")
            delContact(numero, contactos)
            listContacts(contactos)
        elif op == "N":
            num = input("digite o numero")
            proContact(num,contactos)
        elif op == "P":
            partName = input("digite o nome ou uma parte dele")
            filterPartName(contactos, partName)

        
            

main()
