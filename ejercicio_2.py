import random
nota = random.randint(1, 10)
if nota >= 6:
    print(f"Promocion directa, la nota es {nota}")
elif nota == 4 or nota == 5:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")
