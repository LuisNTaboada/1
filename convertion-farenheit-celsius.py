conversion = input("Quieres convertir de *C - *F / *F - *C ")
farenheit = 0
celsius = 0
while farenheit == celsius:
    if conversion == ("F-C").upper():
        farenheit = float(input("*F: "))
        celsius = (farenheit - 32)/1.8
        print("{}*F = {}*C".format(farenheit, celsius))

    elif conversion == "C-F".upper():
        celsius = float(input("*C: "))
        farenheit = (celsius * 1.8 + 32)
        print("{}*C = {}*F".format(celsius, farenheit))
    else:
        print("que?")


