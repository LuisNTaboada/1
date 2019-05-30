#determinar el numero mas grande de una serie de 10 numeros

numeros = []
numeros_del_usuario = ""

while len(numeros) < 10:
    while not numeros_del_usuario.isdigit():
        numeros_del_usuario = input("Dime un numero: ")
    numeros.append(int(numeros_del_usuario))
    numeros_del_usuario = ""
    print("Kmara")

print(numeros)

numero_mas_grande = numeros[0]

for numero in numeros:
    if numero_mas_grande < numero:
        numero_mas_grande = numero

print("El numero mas grande es {}".format(numero_mas_grande))



