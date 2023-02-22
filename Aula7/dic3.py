# The periodic table of elements.
periodicTable = {
   "H": "Hydrogen", "C": "Carbon", "O": "Oxygen",
   "Fe": "Iron", "Au": "Gold", "Na": "Sodium",
   "Ag": "Silver", "Pb": "Lead", "Pu": "Plutonimum"
}



element = input("Enter symbol (or Q to quit): ").upper()
if element != "Q":
    fim = periodicTable.get(element, "invalid")
    print(fim)

    #continuar daqui 

    



