

accion_escogida = 0
felicidad_eugenio = 0

#Instrucciones
print("Eugenio esta triste. Ayudalo a animarse")
print("Para animarlo puedes: \n -Darle de comer (+1) \n -Dejarlo jugar play (+2) \n -Hacerlo reir (+3) \n -Darle mota (+5)")
print("Para animarlo escoge una de las opciones anteriores. Dependiendo de cual escogas se le añadiran corazones.\n")
print("La cantidad de corazones que se le añadan dependera de que accion escogas.")
print("Cuando alcances la cantidad de 20 o mas corazones habras conseguido alegrar a Eugenio. \n Entonces, empieza:")

#juego

while felicidad_eugenio < 20:
#acciones
    accion_escogida = input("Que quieres hacer para animar a Eugenio?: ").upper()
    if accion_escogida == "DARLE MOTA":
        print("(+5)")
        felicidad_eugenio += 5

    elif accion_escogida == "DARLE DE COMER":
        print("(+1)")
        felicidad_eugenio += 1

    elif accion_escogida == "DEJARLO JUGAR PLAY":
        print ("(+2)")
        felicidad_eugenio += 2

    elif accion_escogida == "HACERLO REIR":
        print("(+3)")
        felicidad_eugenio += 3

    print("Eugenio tiene {} corazones".format(felicidad_eugenio))

print("Ganaste. Hiciste feliz a Eugenio")








