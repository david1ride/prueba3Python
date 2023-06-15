import funciones

def mostrar_menu():
    print("----- Registro de Afiliados -----")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Listar únicamente solteros")
    print("4. Salir")

def obtener_datos_persona():
    rut = input("Ingrese el Rut: ")
    nombre = input("Ingrese el Nombre: ")
    edad = int(input("Ingrese la Edad: "))
    estado_civil = input("Ingrese el Estado Civil (C = Casado, S = Soltero, V = Viudo): ")
    fecha_afiliacion = input("Ingrese la Fecha de Afiliación: ")
    return rut, nombre, edad, estado_civil, fecha_afiliacion

def grabar_persona():
    rut, nombre, edad, estado_civil, fecha_afiliacion = obtener_datos_persona()
    if funciones.validar_rut(rut) and edad > 18 and estado_civil in ['C', 'S', 'V']:
        funciones.grabar_datos_persona(rut, nombre, edad, estado_civil, fecha_afiliacion)
        print("Datos de persona grabados exitosamente.")
    else:
        print("Error en los datos ingresados.")

def buscar_persona():
    rut = input("Ingrese el Rut de la persona a buscar: ")
    persona = funciones.buscar_persona_por_rut(rut)
    if persona:
        print("Datos de la persona:")
        print("Rut:", persona[0])
        print("Nombre:", persona[1])
        print("Edad:", persona[2])
        print("Estado Civil:", persona[3])
        print("Fecha de Afiliación:", persona[4])
    else:
        print("No se encontró ninguna persona con ese Rut.")

def listar_solteros():
    solteros = funciones.listar_personas_solteras()
    print("Ficha de datos de personas solteras:")
    for persona in solteros:
        print("Rut:", persona[0])
        print("Nombre:", persona[1])
        print("Edad:", persona[2])
        print("Estado Civil:", persona[3])
        print("Fecha de Afiliación:", persona[4])
    print("Cantidad de registros listados:", len(solteros))
    maxima_edad = max(solteros, key=lambda x: x[2])[2]
    print("Máxima edad registrada:", maxima_edad)

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        grabar_persona()
    elif opcion == "2":
        buscar_persona()
    elif opcion == "3":
        listar_solteros()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
