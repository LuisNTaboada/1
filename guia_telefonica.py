guia = dict()
salir = False

while not salir:
    accion = input("Añadir Numero(A)/Pedir numero(P)/Salir(S) ").upper()
        #Añadir
    if accion == "A":
        print("Añadir numero de telefono")
        name = input("Nombre: ")
        number = input("Numero ")
        guia[name] = number

        #Pedir
    elif accion == "P":
        print("Quieres ver el numero de alguien")
        name = input("De quien quieres saber el numero? ")
        print(guia[name])


         # Salir
    elif accion == "S":
        salir = True

