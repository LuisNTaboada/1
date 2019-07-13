import datetime

AVARAGE_LIFESPAN = 80
SMOKER_PENALIZATION = 10
DRINKER_PEALIZATION = 10
SEDENTARY_PENALIZATION = 20

def print_with_underscores(message):
    print(message)
    print(len(message) * "-")

print_with_underscores("Adivina cuanto te queda de vida")
print("Completa esta encuesta")

birth_date = input("Cual es tu fecha de nacimineto? (dd/mm/yyyy) ")

birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

def ask_yes_no(message):
    response = None
    while response != "S" and response != "N":
        response = input(message + "[S/N]")
        return response == "S"

years_lost = 0


if ask_yes_no("Fumas? "):
    years_lost += SMOKER_PENALIZATION

if ask_yes_no("Bebes? "):
   years_lost += DRINKER_PEALIZATION

if not ask_yes_no("Haces deporte? "):
    years_lost +=SEDENTARY_PENALIZATION

lifespan = AVARAGE_LIFESPAN - years_lost

death_day = birth_date + datetime.timedelta(days= lifespan*360)

days_2_death = death_day - datetime.datetime.now()

death_day = birth_date + datetime.timedelta(days= lifespan*360)
print(f"Fecha de muerte: {death_day.strftime()}, te queda {days_2_death}")



