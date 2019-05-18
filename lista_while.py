
mi_lista = []
input_usuario = ""
input_usuario = input("Que quieres comprar? (Escribe Fin para terminar): ")

while input_usuario != "Fin":
    mi_lista.append(input_usuario)
    input_usuario = input("Que quieres comprar? (Escribe Fin para terminar): ")



largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1
