print("Ejercicio 3.1: Realiza las siguientes operaciones con listas:")
print(" ")

lista = [1, 2, 3, 4, 5]
# a) Añade el número 6 al final
lista.append(6)
print(lista)

# b) Inserta el número 0 al inicio
lista.insert(0,0)
print(lista)

# c) Elimina el número 3
lista.pop(3)
print(lista)

# d) Ordena la lista en orden descendente
lista.sort(reverse=True)
print(lista)

# e) Crea una nueva lista con los elementos duplicados
print(lista[::1]) #no entendi si esto lo que pedia el ejercicio xd

print(" ")
print("Ejercicio 3.2: Dada una lista, encuentra el segundo número más grande.")

numeros = [23, 54, 12, 87, 32, 45, 98, 76]

# Encuentra y muestra el segundo valor más alto
numeros.sort(reverse=True)
nmayor= numeros[1]
print(nmayor)

print(" ")
print("Ejercicio 3.3: Crea un programa que cuente la frecuencia de cada palabra en un texto.")
#texto a usar
texto = "Python es un lenguaje de programación. Python es fácil de aprender."

# Resultado esperado: {"Python": 2, "es": 2, "un": 1, "lenguaje": 1, "de": 1, "programación.": 1, "fácil": 1, "aprender.": 1} 
from collections import Counter
palabras=texto.split()
print(Counter(palabras)) #tambien es posible usar el metodo dict() de esta forma: dict(Counter(palabras)) para crear un diccionario (y puede guardarse en una variable tambien)

print(" ")
print("3.4: Manipula un diccionario con información de estudiantes:")

estudiantes = {
"Juan": {"edad": 20, "curso": "Python", "promedio": 8.5},
"María": {"edad": 22, "curso": "Java", "promedio": 9.0},
"Pedro": {"edad": 21, "curso": "Python", "promedio": 7.8}
}

# a) Agrega un nuevo estudiante
#solicitud de datos del nuevo estudiante
nombre = input("Ingrese el nombre del nuevo estudiante: ")
edad = int(input("Ingrese la edad: "))
curso = input("Ingrese el curso: ")
promedio = float(input("Ingrese el promedio: "))

#nuevo estudiante
estudiantes[nombre] = {"edad": edad, "curso": curso, "promedio": promedio}

# b) Actualiza el promedio de Juan a 9.0
nombre_promedio = input("Ingrese el nombre del estudiante al que desea cambiarle el promedio: ")
nuevo_promedio = input(f"Ingrese el nuevo promedio del estudiante {nombre_promedio}: ")
estudiantes[nombre_promedio]["promedio"] = nuevo_promedio

# c) Muestra solo los estudiantes de Python
estudiantes_python = {nombre: datos for nombre, datos in estudiantes.items() if datos["curso"] == "Python"}
print("Estudiantes del lenguaje Python:", estudiantes_python)

# d) Calcula el promedio de edad de todos los estudiantes
for i in estudiantes.values():
    promedio=i["edad"]/len(estudiantes)
print(promedio)