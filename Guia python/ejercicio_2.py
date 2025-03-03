print("Ejercicio 2.1: Escribe un programa que determine si un número es par o impar, positivo o negativo.")
print(" ")
# Dado un número, imprime:
# - "Par positivo" si es par y mayor que cero
# - "Par negativo" si es par y menor que cero
# - "Impar positivo" si es impar y mayor que cero
# - "Impar negativo" si es impar y menor que cero
# - "Cero" si es exactamente cero
numero=int(input("Ingresa un numero para ser evaluado: "))

if numero == 0:
    print("Cero")
elif numero % 2 == 0:
    if numero < 0:
        print("par negativo")
    else:
        print("par positivo")
else:
    if numero < 0:
        print("impar negativo")
    else:
        print("impar positivo")

print(" ")
print("Ejercicio 2.2: Implementa un programa que imprima los primeros n números de la serie Fibonacci.")
# Escribe una función fibonacci(n) que devuelva los primeros n números de la serie.

secuencia = []
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def mostrar_en_consola(limit):
    for i in range(limit):
        print(fibonacci(i))

n=fibonacci(int(input("ingrese un numero en el cual desee iniciar la secuencia fibonacci ")))
limit=mostrar_en_consola(int(input("Ingrese límite de iteraciones a realizar en la secuencia fibonacci")))

print(" ")
print("Ejercicio 2.3: Escribe un programa que recorra una lista e imprima solo los números pares.")
# Imprime solo los números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numeros:
    if i % 2 == 0:
        print(i)

print("")
print(" ")