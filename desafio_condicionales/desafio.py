tarifa_fija = 7000
tarifa_agua = 200
iva = 0.21
descuento = 0
recargo = 0
agua_consumida = int(input("Ingresar la cantidad de metros cubicos de agua consumidos: "))
valor_agua = agua_consumida * tarifa_agua
tipo_cliente = input("Ingresar su tipo (Residencial, Comercial, Industrial): ")

if tipo_cliente == "Residencial":
    if agua_consumida > 80:
        recargo += 0.15
    elif agua_consumida < 30:
        descuento += 0.1
elif tipo_cliente == "Comercial":
    if agua_consumida > 300:
        descuento += 0.12
    elif agua_consumida > 150:
        descuento += 0.08
    elif agua_consumida < 50:
        recargo += 0.05
elif tipo_cliente == "Industrial":
    if agua_consumida > 1000:
        descuento += 0.3
    elif agua_consumida > 500:
        descuento += 0.2
    elif agua_consumida < 200:
        recargo += 0.1

if tipo_cliente == "Residencial" and valor_agua < 35000:
    descuento += 0.05

total_sin_iva = valor_agua + valor_agua * recargo - valor_agua * descuento
total = total_sin_iva + total_sin_iva * iva
print("---------------------------------------")
print(f"Subtotal de consumo: {valor_agua}")
print(f"Su bonificacion es del {descuento * 100}%")
print(f"Su recarga es del {recargo * 100}%")
print(f"Su tarifa antes de impuestos es: ${total_sin_iva}")
print(f"El total a pagar es de: ${total}")
print("---------------------------------------")
