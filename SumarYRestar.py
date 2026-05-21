print("CALCULADORA")
print("1. Sumar")
print("2. Restar")

opcion = int(input("Seleccione una opción: "))

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == 1:
    resultado = num1 + num2
    print("La suma es:", resultado)

elif opcion == 2:
    resultado = num1 - num2
    print("La resta es:", resultado)

else:
    print("Opción no válida")