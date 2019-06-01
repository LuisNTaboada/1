
numero_materias = 0
pregunta = ""
calif_materia = 0


materias = ["fisica", "matemaricas", "historia", "foce", "espanol", "ingles", "artes", "dibujo", "computacion", "edu_fisica","tutoria"]

for materia in materias:
    numero_materias += 1
    pregunta = input("Que calificacion sacaste en {}? ".format(materia))
    calif_materia += int(pregunta)
    calif_final = calif_materia

calif_final = calif_final/numero_materias
print("Tu promedio final es de {}".format(round(calif_final, 2)))




