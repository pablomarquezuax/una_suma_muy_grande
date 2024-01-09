# Función para sumar los elementos del array
def sumar_array(array):
    suma = sum(array)
    return suma

# Función principal
def aVeryBigSum():
    # Input del usuario: introducir los números separados por espacios
    input_numeros = input("Introduce un array de números separados por espacios: ")

    # Convertir la entrada a una lista de números
    array_numeros = [float(num) for num in input_numeros.split()]

    # Mostrar el array
    print("Array de números:", array_numeros)

    # Calcular y mostrar la suma de los números
    suma_total = sumar_array(array_numeros)
    print("Suma total (long):", suma_total)

# Ejecutar el programa principal
if __name__ == "__main__":
   aVeryBigSum()
