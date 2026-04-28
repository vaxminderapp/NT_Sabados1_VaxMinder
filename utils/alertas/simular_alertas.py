from datetime import datetime, timedelta   
import random 

def simular_alertas(numeroAlertas):
    
    # Semillas de datos
    listasTiposAlerta = ["refuerzo", "recordatorio", "vencimiento"]
    
    listaMensajes = [
        "Recuerde completar el refuerzo de vacunación",
        "Su vacuna está próxima a vencer",
        "Es hora de aplicarse la siguiente dosis",
        "Aviso: Su registro de vacunación vence en 30 días",
        "Recordatorio: Debe completar su esquema de vacunación",
        "Su vacuna de refuerzo está disponible",
        "Alerta: Esquema de vacunación incompleto",
        "Debe agendar cita para refuerzo de vacunación",
        "Su documento de vacunación vence próximamente",
        "Recuerde actualizar su información de vacunación"
    ]
    
    listaEstados = ["pendiente", "enviada", "leida", "descartada"]
    
    # Fechas
    fechaInicial = datetime(2026, 1, 1)
    fechaEnvioInicial = datetime(2026, 1, 15)
    
    alertas = []
    
    for id_alerta in range(1, numeroAlertas + 1):
        # ID usuario (referencia a usuarios existentes)
        id_usuario = random.randint(10000000, 99999999)
        
        # ID registro (puede ser NULL)
        id_registro = random.randint(1, 1000) if random.random() > 0.3 else None
        
        # Tipo de alerta
        tipo_alerta = random.choice(listasTiposAlerta)
        
        # Fecha de alerta (entre enero y marzo de 2026)
        diasAleatorios = random.randint(0, 90)
        fecha_alerta = fechaInicial + timedelta(days=diasAleatorios)
        
        # Mensaje
        mensaje = random.choice(listaMensajes)
        
        # Estado
        estado = random.choice(listaEstados)
        
        # Fecha de envío (SOLO si no está pendiente)
        fecha_envio = None
        if estado != "pendiente":
            diasEnvio = random.randint(0, 45)
            fecha_envio = fechaEnvioInicial + timedelta(days=diasEnvio)
            fecha_envio = fecha_envio.strftime("%Y-%m-%d %H:%M:%S")
        
        alerta = {
            "id_alerta": id_alerta,
            "id_usuario": id_usuario,
            "id_registro": id_registro,
            "tipo_alerta": tipo_alerta,
            "fecha_alerta": fecha_alerta.strftime("%Y-%m-%d"),
            "mensaje": mensaje,
            "estado": estado,
            "fecha_envio": fecha_envio
        }
        
        alertas.append(alerta)
    
    return alertas


# Ejemplo de uso
if __name__ == "__main__":
    alertas_simuladas = simular_alertas(10)
    for alerta in alertas_simuladas:
        print(alerta)
