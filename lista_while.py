
mi_lista = []
input_usuario = ""
input_usuario = input("Que quieres comprar? (Escribe Fin para terminar): ")

while input_usuario != "Fin":
    mi_lista.append(input_usuario)
    input_usuario = input("Que quieres comprar? (Escribe Fin para terminar): ")

for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print ("Esta es la lista de la compra :)")