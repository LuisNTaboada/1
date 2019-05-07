
print("Pos, tu dime un numero sin que tu(s) compa(s) lo vean y despues intentan adivinar")
number = int(input("Dime un numero del 1-10: "))
guess_number = int(input("Cual fue el numero?: "))

while guess_number != number:
    if guess_number == number:
        guess_number == True
    else:
        guess_number == False
        guess_number = int(input("No. ¿Cual fue el numero?"))

print("SIMON! Ese fue el numero. ahre")






