resultado = 0
numero_usuario = 0
numero_usuario = int(input("De que numero quieres la tabla (Del 1 al 15): "))

for multiplo in range(1, 16):
    resultado = numero_usuario * multiplo
    if (resultado % 2) == 0:
        print("Este es multiplo de 2: {} x {} = {}".format(numero_usuario, multiplo, resultado))
    else:
        print("{} x {} = {}".format(numero_usuario, multiplo,resultado))

