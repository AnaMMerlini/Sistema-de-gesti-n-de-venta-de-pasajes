"""11 - Sistema de venta de pasajes:
Implementar un sistema que gestione las ventas de pasajes de micro a distintos destinos y en diferentes fechas,
utilizando matrices, listas y diccionarios para mantener la información. Esta debe almacenarse en archivos para permitir
su posterior recuperación. Aplicar GIT para control de versiones y recursividad para realizar las búsquedas."""
# Función para validar el destino
def validar_destino(destinos, destino):
    #Función lambda para tener el destino en formato oración
    destino_capitalizado = lambda s: s.capitalize()
    destino = destino_capitalizado(destino)
    while destino not in destinos:
        print("Destino incorrecto")
        destino = destino_capitalizado(input("Ingresar destino correcto: "))
    return destino

# Función para validar el día y mes de la fecha de ida
def validar_fecha_ida(fecha_ida):
    dia = fecha_ida // 100  # Separa el día
    mes = fecha_ida % 100    # Separa el mes
    while dia < 1 or dia > 31 or mes < 10 or mes > 12 or (dia == 31 and mes == 11):
        print("La fecha es incorrecta")
        fecha_ida = int(input("Ingresar fecha válida de ida en formato ddmm: "))
        dia = fecha_ida // 100
        mes = fecha_ida % 100
    return fecha_ida

# Función para validar la fecha de regreso
def validar_fecha_regreso(fecha_ida, fecha_regreso):
    dia_ida = fecha_ida // 100
    mes_ida = fecha_ida % 100
    dia_regreso = fecha_regreso // 100
    mes_regreso = fecha_regreso % 100
    while fecha_regreso <= fecha_ida or dia_regreso < 1 or dia_regreso > 31 or mes_regreso < 10 or mes_regreso > 12 or (dia_regreso == 31 and mes_regreso == 11):
        print("La fecha de regreso es incorrecta")
        fecha_regreso = int(input("Ingresar fecha válida de regreso en formato ddmm: "))
        dia_regreso = fecha_regreso // 100
        mes_regreso = fecha_regreso % 100
    return fecha_regreso

# Función para validar el DNI del pasajero
def validar_dni(dni):
    while dni < 1000000 or dni > 70000000:
        print("DNI no válido")
        dni = int(input("Ingresar número de DNI válido: "))
    return dni

# Función para agregar al pasajero
def agregar_pasajero(pasajeros, nombre, dni):
    pasajero = {"nombre": nombre, "dni": dni}
    pasajeros.append(pasajero)

# Función para verificar la disponibilidad de micros
def disponibilidad(micros, destino, fecha_ida):
    for micro in micros:
        if micro["destino"] == destino and micro["capacidad"] > 0:
            if fecha_ida in micro["fechas"]:
                micro["capacidad"] -= 1  # Reducir la capacidad en 1 al reservar
                return True
    return False

# Programa Principal
#Diccionario con las claves de destino, capacidad y fechas
#Convertir el día en una cadena y ponerlo a la derecha, añadiendo un '0' a la izquierda si el día es menor que 10
micros = [
    {"destino": "Bariloche", "capacidad": 42, "fechas": [f"{str(dia).rjust(2, '0')}-10" for dia in range(1, 32)] + #mes de octubre
                                                 [f"{str(dia).rjust(2, '0')}-11" for dia in range(1, 31)] + #mes de noviembre
                                                 [f"{str(dia).rjust(2, '0')}-12" for dia in range(1, 32)]}, #mes de diciembre
    {"destino": "Mendoza", "capacidad": 42, "fechas": [f"{str(dia).rjust(2, '0')}-10" for dia in range(1, 32)] +
                                                     [f"{str(dia).rjust(2, '0')}-11" for dia in range(1, 31)] +
                                                     [f"{str(dia).rjust(2, '0')}-12" for dia in range(1, 32)]},
    {"destino": "Neuquén", "capacidad": 42, "fechas": [f"{str(dia).rjust(2, '0')}-10" for dia in range(1, 32)] +
                                                       [f"{str(dia).rjust(2, '0')}-11" for dia in range(1, 31)] +
                                                       [f"{str(dia).rjust(2, '0')}-12" for dia in range(1, 32)]},
    {"destino": "Córdoba", "capacidad": 42, "fechas": [f"{str(dia).rjust(2, '0')}-10" for dia in range(1, 32)] +
                                                      [f"{str(dia).rjust(2, '0')}-11" for dia in range(1, 31)] +
                                                      [f"{str(dia).rjust(2, '0')}-12" for dia in range(1, 32)]},
]
#Lista con los destinos
destinos = ["Bariloche", "Mendoza", "Neuquén", "Córdoba"]

pasajeros = []
#Lista de pasajeros con su nombre y DNI
print("Posibles destinos:", " - ".join(destinos))
print()
#Información que se necesita de la venta y llamar a las funciones
destino = input("Ingresar destino: ")
destino = validar_destino(destinos, destino)

fecha_ida = int(input("Ingresar fecha de ida en formato ddmm: "))
fecha_ida = validar_fecha_ida(fecha_ida)

fecha_regreso = int(input("Ingresar fecha de vuelta en formato ddmm: "))
fecha_regreso = validar_fecha_regreso(fecha_ida, fecha_regreso)

nombre = input("Ingresar nombre completo del pasajero: ")
dni = int(input("Ingresar DNI completo del pasajero: "))
dni = validar_dni(dni)

# Formatear fecha en formato "dd/mm"
fecha_ida_formateada = f"{str(fecha_ida // 100).rjust(2, '0')}-{str(fecha_ida % 100).rjust(2, '0')}" #Se une la fecha dd-mm

# Verificar disponibilidad
if disponibilidad(micros, destino, fecha_ida_formateada):
    agregar_pasajero(pasajeros, nombre, dni)
    print(f"Pasajero {nombre} agregado correctamente al micro con destino {destino}.")
else:
    print("No se puede realizar la reserva. No hay disponibilidad.")