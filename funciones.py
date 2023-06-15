registros = []

def validar_rut(rut):
    # Implementa aquí la lógica de validación del RUT
    return True

def grabar_datos_persona(rut, nombre, edad, estado_civil, fecha_afiliacion):
    registros.append((rut, nombre, edad, estado_civil, fecha_afiliacion))

def buscar_persona_por_rut(rut):
    for persona in registros:
        if persona[0] == rut:
            return persona
    return None

def listar_personas_solteras():
    solteros = [persona for persona in registros if persona[3] == 'S']
    return solteros
