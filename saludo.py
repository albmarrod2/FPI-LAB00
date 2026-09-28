from datetime import datetime

hora_actual = datetime.now().hour
nombre = input("Introduzca su nombre:")
if hora_actual < 12 :
    print(f"Buenos dias, {nombre}")
elif 12<= hora_actual <= 20:
    print(f"Buenas tardes, {nombre}")
elif 21 <= hora_actual <= 23:
    print(f"Buenas noches, {nombre}")
else:
    print(f"Hola, {nombre}")