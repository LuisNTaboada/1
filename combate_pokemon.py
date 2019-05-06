
pokemon_elegido = input("contra que pokemon quieres luchar? (Squirtle / Charmander / Bulbasaur:) ").upper()
vida_pikachu = 100
vida_enemigo = 0
daño_pokemon = 0
bola_voltio = 12
chispazo = 6

if pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    daño_pokemon = 10

elif pokemon_elegido == "SQUIRTEL":
    nombre_pokemon = "Squirtle"
    vida_enemigo = 90
    daño_pokemon = 8

elif pokemon_elegido == "BULBASAUR":
    nombre_pokemon = "Bulbasaur"
    vida_enemigo = 100
    daño_pokemon = 9

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vas a usar? (Bola Voltio o Chispazo?): ").upper()

    if ataque_elegido == "BOLA VOLTIO":
        print("{} ha recibido Bola Voltio(-{})".format(nombre_pokemon , bola_voltio))
        vida_enemigo -= bola_voltio

    elif ataque_elegido == "CHISPAZO":
        print("{} ha recibido Chispazo(-{})".format(nombre_pokemon , chispazo))
        vida_enemigo -= chispazo

        vida_pikachu -= daño_pokemon

    print("{} te ha hecho daño (-{})".format(nombre_pokemon, daño_pokemon))
    print("La vida de {} es de {}".format(nombre_pokemon, vida_enemigo))
    print("Te queda {} de vida".format(vida_pikachu))

if vida_enemigo <= 0:
    print ("Ganaste :)")

if vida_pikachu <= 0:
    print("Perdiste :(")

print ("El combate ha terminado")