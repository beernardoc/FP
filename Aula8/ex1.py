 # Devolve o IMC para uma pessoa com peso w e altura h.
def imc(w, h):
    return w/h**2


def main():
    people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

    print("People:", people)

    
    names = [n for n,w,h in people]
    print("Names:", names)
    
   
    imcs = [w/(h**2) for n,w,h in people]
    print("IMCs:", imcs)

    
    tallpeople = [n for n,w,h in people if h > 1.7]
    print("Tall people:", tallpeople)    

   
    midimc = [n for n,w,h in people if w/(h**2) >=18 if w/(h**2) <=25 ]
    print("Mid-IMC:", midimc)


# O programa come�a aqui
main()
