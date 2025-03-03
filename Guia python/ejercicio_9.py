print("Ejercicio 9.1: Valida un correo electrónico")
print(" ")
import re

# Crea una función validar_email que determine si una cadena es un email válido
def validar_email():

    email= input("Ingrese su email para validarlo: ") #puede usar este correo para testear: usuario@dominio.com

    # segun encontre en google, esta es la expresion que se usa para comprobar correos
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    #recibe 2 parametros para comparar si "email" cumple con el patron/expresion
    if re.match(patron, email):
        return "El correo es válido."
    else:
        return "El correo no es válido."
    
test = validar_email()
print(test)

print(" ")
print("Ejercicio 9.2: Extrae información de un texto con patrones:")

def extraer_fechas():
    # Dado un texto con fechas en formato DD/MM/AAAA, extrae todas las fechas
    texto = input("Añada el texto acá") #puede usar este texto para testear: La reunión será el 15/04/2023 y la entrega está programada para el 30/05/2023.

    #lo mismo que con la expresion del correo (google)
    patron = r'\b\d{2}/\d{2}/\d{4}\b'
    
    # Busca todas las coincidencias en el texto
    fechas = re.findall(patron, texto)
    
    return fechas

# Prueba de la función
test2 =extraer_fechas()
print(test2)