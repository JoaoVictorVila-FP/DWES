
from operaciones import suma, resta, multiplicacion, division

def obtener_numeros():
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    return num1, num2

def obtener_operacion():
    
    print("Seleccione el tipo de operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = input("Ingrese el número de la operación deseada (1/2/3/4): ")
    return opcion

while True:
    num1, num2 = obtener_numeros()
    opcion = obtener_operacion()

    if opcion == '1':
        resultado = suma(num1, num2)
    elif opcion == '2':
        resultado = resta(num1, num2)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
    elif opcion == '4':
        resultado = division(num1, num2)
    else:
        print("Opción no válida.")
        continue

    print("El resultado es:", resultado)

    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break




