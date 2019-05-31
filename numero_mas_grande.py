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

largo = 0
media = 0
x = 0
#Saca el largo de la lista sin usar len()
for numero in numeros:
    largo += 1
    x += numero


media = (x)/largo

print("El largo de la lista es {}".format(largo))
print("El numero mas grande es {}".format(numero_mas_grande))
print("Y la media es {}".format(media))




