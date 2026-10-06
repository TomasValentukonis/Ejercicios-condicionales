altura = int(input("Ingresar altura en CM: "))
if altura < 160:
    print("El jugador es Base!")
elif altura >= 160 and altura <= 179:
    print("El jugador es Escolta!")
elif altura >= 180 and altura <= 199:
    print("El jugador es Alero!")
else:
    print("El jugador es Pivot!")
