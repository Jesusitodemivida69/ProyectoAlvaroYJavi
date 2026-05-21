print("CALCULADORA")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Seleccione una opción: "))

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

elif opcion == 3:
    resultado = num1 * num2
    print("La multiplicación es:", resultado)

elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("La división es:", resultado)
    else:
        print("Error: no se puede dividir entre cero")

else:
    print("Opción no válida")