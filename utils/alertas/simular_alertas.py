from datetime import datetime, timedelta
import random


def simular_alertas(numeroAlertas):
    listasTiposAlerta = ["refuerzo", "recordatorio", "vencimiento"]

    mensajes_por_tipo = {
        "refuerzo": [
            "Es hora de aplicarse la siguiente dosis",
            "Su vacuna de refuerzo está disponible",
            "Debe agendar cita para refuerzo de vacunación",
            "Recuerde completar el refuerzo de vacunación",
        ],
        "recordatorio": [
            "Recordatorio: Debe completar su esquema de vacunación",
            "Recuerde actualizar su información de vacunación",
            "Su documento de vacunación vence próximamente",
            "Aviso: Su registro de vacunación vence en 30 días",
        ],
        "vencimiento": [
            "Su vacuna está próxima a vencer",
            "Alerta: Esquema de vacunación incompleto",
            "Su vacuna de refuerzo vence en menos de 3 días",
            "Aviso urgente: vacuna próxima a vencer",
        ],
    }

    hoy = datetime(2026, 4, 29)
    alertas = []

    for id_alerta in range(1, numeroAlertas + 1):
        id_usuario  = random.randint(10000000, 99999999)
        id_registro = random.randint(1, 1000)
        tipo_alerta = random.choice(listasTiposAlerta)

        # Fecha de vencimiento entre 30 dias atras y 60 dias adelante
        dias_offset = random.randint(-30, 60)
        fecha_vencimiento = hoy + timedelta(days=dias_offset)

        # La alerta se programa exactamente 3 dias antes del vencimiento
        fecha_alerta = fecha_vencimiento - timedelta(days=3)

        # La alerta se envia el mismo dia o hasta 1 dia despues de programarse
        fecha_envio = fecha_alerta + timedelta(days=random.randint(0, 1))

        # Estado segun si la fecha de envio ya paso o no respecto a hoy
        if fecha_envio.date() > hoy.date():
            estado = "pendiente"
            # pendiente = aun no llega la fecha, pero ya esta programada
            # fecha_envio ya esta calculada (fecha futura programada)
        else:
            estado = random.choice(["enviada", "leida", "descartada"])

        mensaje = random.choice(mensajes_por_tipo[tipo_alerta])

        alertas.append({
            "id_alerta":        id_alerta,
            "id_usuario":       id_usuario,
            "id_registro":      id_registro,
            "tipo_alerta":      tipo_alerta,
            "fecha_vencimiento": fecha_vencimiento.strftime("%Y-%m-%d"),
            "fecha_alerta":     fecha_alerta.strftime("%Y-%m-%d"),
            "fecha_envio":      fecha_envio.strftime("%Y-%m-%d"),
            "mensaje":          mensaje,
            "estado":           estado,
        })

    return alertas


if __name__ == "__main__":
    for a in simular_alertas(5):
        print(a)
