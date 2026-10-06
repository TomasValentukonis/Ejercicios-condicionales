estacion = input("Ingresar estacion del año (sin mayusculas): ")
lugar = input("Ingrese el lugar a viajar (sin mayusculas): ")
match estacion:
    case "invierno":
        if lugar == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if lugar == "mar del plata" or lugar == "cataratas":
            print("Se viaja")
        else:
            print("No se viaja")
    case "otoño": 
        print("Se viaja")
    case "primavera":
        if lugar != "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case _:
        print("No se viaja")
