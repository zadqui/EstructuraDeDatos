#Lista estática
calificaciones = [0] * 5

for i in range(5):
    calificaciones[i] = int(input(f"Captura la calificación {i + 1}: "))


print("\nCalificaciones ingresadas:")
for i, cal in enumerate(calificaciones, start=1):
    print(f"Calificación {i}: {cal}")

print("-------------------")

# Lista dinámica 
frutas = []  


frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Uvas")
frutas.append(3)

print(frutas)

elemento = frutas[2] * frutas[4]
print("La multiplicación es:", elemento)

frutas.pop(0)  
frutas.pop(1)  


frutas.append("Sandía")

print(frutas)
