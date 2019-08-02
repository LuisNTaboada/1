from time import sleep
import datetime

NIGHT_STARTS = 20
DAY_STARTS = 6
HOUR_DURATION = 1

def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    current_time = datetime.datetime.now()
    is_night = False


    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours= 1)
        light_change = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_change = True
        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_true = True

        if light_change:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")

        write_file_and_screen("Ahora es {}".format(current_time), "horas.txt")





if __name__ == "__main__":
    main()
