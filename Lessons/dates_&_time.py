import datetime

date = datetime.date(2025, 7, 25) # pone el formato fecha por defecto
time = datetime.time(9, 14, 0) # pone el formato de la hora por defecto

today = datetime.date.today() # imprime el día de hoy en el formato por defecto
now = datetime.datetime.now() # imprime fecha y hora en el formato por defecto

now = now.strftime("%d-%m-%Y %H:%M:%S") # Así podemos elegir el formato, d, m, Y son la fecha


target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")