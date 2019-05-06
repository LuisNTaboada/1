
first_number = 0
second_number = 0
result = 0

operation_type = input("Que operacion quieres realizar? (multiplicacion / division / suma / resta?: ").upper()
first_number = float(input("Dime el primer numero:  "))
second_number = float(input("Dime el segundo numero: "))

if operation_type == "SUMA":
    result = (first_number + second_number)
    print(result)

elif operation_type == "RESTA":
    result = (first_number - second_number)
    print(result)

elif operation_type == "MULTIPLICACION":
    result = (first_number * second_number)
    print (result)

elif operation_type == "DIVISION":
    result = (first_number/second_number)
    print(result)

else:
    print("Bro, solo hago sumas, restas, divisiones y multiplicaciones")