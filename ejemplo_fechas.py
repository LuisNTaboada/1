import datetime
def dia_faltante(X):
    year = int(input("Año: "))
    month = int(input("Mes? "))
    day = int(input("Dia? "))

    user_date = datetime.datetime(year= year, month= month, day= day)

    remaining_time = user_date - datetime.datetime.now()

    print(f"Faltan {remaining_time.days} dias y {int(remaining_time.seconds / 3600 )} horas ")

    print(datetime.datetime.now() + remaining_time)

manana = datetime.datetime.now() + datetime.timedelta(days= 1)
manana_medianoche = datetime.datetime(year= manana.year, month= manana.month, day= manana.day)
hoy = datetime.datetime.now()
falta_manana = manana_medianoche - hoy
print(f"Mañana es {manana}")
print(f"Faltan {falta_manana.total_seconds()/3600} horas para mañana :00")




