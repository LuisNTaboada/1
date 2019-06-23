
def reverse_string(string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed

string_volteada = reverse_string("Hola")
print(string_volteada)



#Numero mas grande

def biggest_number_user(numeros):
    nmrs = []
    while len(nmrs) <= 3:
        pregunta_numeros = int(input("Numero? "))
        nmrs.append(pregunta_numeros)
        pregunta_numeros = ""
    biggest_number = nmrs[0]

    for numero in nmrs:
        if numero > biggest_number:
            biggest_number = numero
    print(f"el numero mas grande es {biggest_number}")

biggest_number_user(1)

def biggest_number_funct(numeros):
    biggest_number = numeros[0]
    for numero in numeros:
        if numero > biggest_number:
            biggest_number = numero

    print(f"el numero mas grande es {biggest_number}")

biggest_number_funct([1, 2, 3, 1, 6])




