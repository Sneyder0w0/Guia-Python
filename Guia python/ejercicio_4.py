print("Ejercicio 4.1: Crea una función que reciba un número variable de argumentos y devuelva su suma.")
print(" ")

# Crea la función suma_total que pueda recibir cualquier cantidad de números
# Ejemplo: suma_total(1, 2, 3, 4) debe devolver 10
def suma_total():
    numeros = []
    while True:
        n_numero = int(input("Añada un número: "))
        numeros.append(n_numero)
        pregunta = input("¿Desea añadir otro número? (Si/No): ").strip().capitalize()
        if pregunta == "No":
            break
    
    return sum(numeros)

resultado = suma_total()
print(f"La suma total es: {resultado}")

print(" ")
print("Ejercicio 4.2: Implementa una función decoradora que mida el tiempo de ejecución de otra función.")
