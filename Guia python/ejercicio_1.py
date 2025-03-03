#Ejercicio 1.1: Identifica el tipo de dato en cada variable:
print("Ejercicio 1.1 realizado en el mismo codigo (con comentarios)")
a = 5 #int
b = 3.14 #float
c = "Python" #str
d = [1, 2, 3] #list
e = (4, 5, 6) #tupla
f = {"nombre": "Juan", "edad": 30} #diccionario
g = {1, 2, 3} #set
h = True #bool

print(" ")
print("Ejercicio 1.2: Realiza conversiones entre tipos de datos:")
# Convierte lo siguiente:

# - El entero 10 a flotante
numero=float(10) #usaré la variable "numero" para todos los ejercicios
print(numero)

# - El flotante 7.5 a entero
numero=int(7.5)
print(numero)

# - La cadena "25" a entero
numero=int("25")
print(numero)

# - La lista [1, 2, 3] a tupla
lista=tuple([1,2,3])
print(lista)

# - La tupla (4, 5, 6) a lista
tupla=list((4,5,6))
print(tupla)

# - La lista [1, 2, 2, 3, 4, 4] a conjunto
lista=set([1,2,2,3,4,4])
print(lista)

print(" ")
print("Ejercicio 1.3: Resuelve las siguientes expresiones y determina su resultado:")
# Aritmética
a = 10 + 5 * 2 - 8 / 4
b = (10 + 5) * (2 - 8) / 4

print(a)
print(b)

# Asignación
c = 10
print(c)

c += 5
print(c)

c *= 2
print(c)

c /= 5
print(c)

# Comparación
d = 10 > 5
print(d)

e = 10 != 10
print(e)

f = "abc" == "abc"
print(f)

# Lógica
g = (10 > 5) and (7 < 12)
print(g)

h = (10 < 5) or (7 > 12)
print(h)

i = not (10 > 5)
print(i)
