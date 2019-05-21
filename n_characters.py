#Contador de caracteres
phrase = input("Pus dime una frase: ")

vocals = ["a", "e", "i", "o", "u"]
n_consonants = 0
n_vocals = 0
n_punctuations = 0
n_spaces = 0
punctuations_marks = [".", ","]
spaces = " "

for character in phrase:
    if character in vocals:
        n_vocals += 1
    elif character in punctuations_marks:
        n_punctuations += 1
    elif character in spaces:
        n_spaces += 1
    else:
        n_consonants += 1

print("vocales = {} y consonantes = {}".format(n_vocals, n_consonants))
print("espacios = {}".format(n_spaces))
print("signos de puntuacion = {}".format(n_punctuations))
print("Total de caracteres = {}".format(len(phrase)))



