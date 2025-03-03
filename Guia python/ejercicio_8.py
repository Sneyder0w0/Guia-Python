print("Ejercicio 8.1: Lee y escribe en un archivo de texto:")
print(" ")
# Crea una función que reciba una lista de nombres y los guarde en un archivo
lista_nombres=[]
def añadir_nombres():
    while True:
        pregunta = input("Desea añadir un nombre? si/no: ").capitalize()
        print(" ")
        if pregunta == "Si":
            nuevo_nombre= input("Ingrese el nombre que desea añadir: ")
            lista_nombres.append(nuevo_nombre)
            print(f"Lista de nombres actual: {lista_nombres}")
        else:
            with open("ejercicio_8.txt", "w+") as archivo:
                archivo.write(str(lista_nombres))
            break

#prueba de funcion "añadir_nombres()"
test = añadir_nombres()

# Crea otra función que lea el archivo y devuelva la lista de nombres
def leer_nombres():
    with open("ejercicio_8.txt","r") as archivo:
        for i in archivo:
            print(i)
#prueba de funcion "leer_nombres()"
test2 = leer_nombres()