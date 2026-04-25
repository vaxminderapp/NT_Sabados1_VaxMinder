from datetime import datetime, timedelta   
import random 

def simular_centros_medicos(numeroCentros):
    
    # Semillas de datos
    listaNombresCentros = [
        "Centro de Salud San Juan", "Clínica Medellín", "Hospital Metropolitano",
        "Centro Médico del Norte", "Clínica Universitaria", "Hospital San Vicente",
        "Centro de Atención Rápida", "Clínica del Caribe", "Hospital Infantil",
        "Centro de Especialidades", "Clínica Privada", "Hospital General",
        "Centro de Vacunación Central", "Clínica Materno Infantil", "Hospital Regional",
        "Centro Médico Sur", "Clínica San José", "Hospital de Día",
        "Centro de Salud Popular", "Clínica Diagnóstica"
    ]
    
    listaCiudades = [
        "Medellín", "Bogotá", "Cali", "Barranquilla", "Cartagena",
        "Santa Marta", "Cúcuta", "Bucaramanga", "Pereira", "Manizales",
        "Armenia", "Ibagué", "Neiva", "Popayán", "Pasto"
    ]
    
    listaTiposCentros = ["Hospital", "Clínica", "Centro de salud"]
    
    centros = []
    
    for id_centro in range(1, numeroCentros + 1):
        # Nombre del centro
        nombre = random.choice(listaNombresCentros)
        
        # Ciudad
        ciudad = random.choice(listaCiudades)
        
        # Dirección simulada
        numero_calle = random.randint(1, 999)
        letra = random.choice(["A", "B", "C", ""])
        numero_carrera = random.randint(1, 150)
        numero_interseccion = random.randint(1, 200)
        direccion = f"Calle {numero_calle}{letra} #{numero_carrera}-{numero_interseccion}, {ciudad}"
        
        # Teléfono simulado (10 dígitos)
        telefono = f"(6) {random.randint(1000000, 9999999)}"
        
        # Tipo de centro
        tipo_centro = random.choice(listaTiposCentros)
        
        centro = {
            "id_centro": id_centro,
            "nombre_centro": nombre,
            "direccion": direccion,
            "ciudad": ciudad,
            "telefono": telefono,
            "tipo_centro": tipo_centro
        }
        
        centros.append(centro)
    
    return centros


# Ejemplo de uso
if __name__ == "__main__":
    centros_simulados = simular_centros_medicos(10)
    for centro in centros_simulados:
        print(centro)
