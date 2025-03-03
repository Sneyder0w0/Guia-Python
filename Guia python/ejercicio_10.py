print("Ejercicio 10.1: Utiliza la biblioteca datetime:")
print(" ")

from datetime import *
# Escribe funciones para:
# - Calcular la edad exacta (años, meses, días) a partir de una fecha de nacimiento
def calcular_edad(nacimiento):
    
    #fecha actual
    fecha_actual = date.today()

    #calculos para el usuario
    años = fecha_actual.year - nacimiento.year
    meses = fecha_actual.month - nacimiento.month
    dias = fecha_actual.day - nacimiento.day
    
    #esto sirve para regresar una fecha exacta, comprobando correctamente los dias vividos, los meses y los años
    if dias < 0:
        meses -= 1
        ultimo_mes = (fecha_actual.replace(day=1) - timedelta(days=1)).day  # Último día del mes anterior
        dias += ultimo_mes

    if meses < 0:
        años -= 1
        meses += 12

    return f"Tienes {años} años, {meses} meses y {dias} dias"

# - Determinar cuántos días faltan para el próximo cumpleaños
def proximo_cumple(nacimiento):

    #fecha actual
    fecha_actual = date.today()

    #fecha en teoria de su proximo cumpleaños
    proximo_cumple = date(fecha_actual.year, nacimiento.month, nacimiento.day)

    #esto sirve para comprobar si su cumpleaños será este año o el proximo
    if proximo_cumple < fecha_actual:
        proximo_cumple = date(fecha_actual.year + 1, nacimiento.month, nacimiento.day)

    dias_restantes = (proximo_cumple - fecha_actual).days
    return f"Faltan {dias_restantes} días para tu próximo cumpleaños."

#Peticion de datos al usuario
print("Ingresa tu fecha de nacimiento separada por guiones")
fecha_nacimiento = input("Ingresa tu fecha de nacimiento en el formato 'YYYY-MM-DD': ")
nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()

#testeo funcion "calcular_edad"
test = calcular_edad(nacimiento)
print(test)

#testeo funcion "proximo_cumple()"
test2 = proximo_cumple(nacimiento)
print(test2)

print(" ")
print("Ejercicio 10.2: Usa la biblioteca random:")

from random import *
import string

# Implementa un generador de contraseñas que:
def generar_contra():

    # - Cree contraseñas de longitud personalizable
    longitud = int(input("Ingrese la longitud de la contraseña: "))

    #esto asegura que tendrá minimo 4 caracteres.
    if longitud < 4:
        return "La contraseña debe tener al menos 4 caracteres."

    # - Incluya letras mayúsculas, minúsculas, números y símbolos
    # - Garantice al menos un carácter de cada tipo
    # esto garantiza que almenos un caracter de cada tipo y la longitud no puede ser menor a 4 debido a que debe incluir si o si 1 caracter de los 4 tipos solicitados
    mayus = choice(string.ascii_uppercase)
    minus = choice(string.ascii_lowercase)
    num = choice(string.digits)
    simb = choice(string.punctuation)

    #genera el resto de la contraseña 
    resto_contra = [choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud)]
    contraseña = [mayus, minus, num, simb] + resto_contra    
    shuffle(contraseña)
    
    return "Su contraseña es: " + "".join(contraseña)

# Prueba de la funcion generar_contra()s
test3 = generar_contra()
print(test3)

