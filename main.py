import pandas as pd

# Zona para importar simulaciones
from utils.alertas.simular_alertas import simular_alertas
from utils.centros_medicos.simular_centros_medicos import simular_centros_medicos
from utils.historialPdf.simular_historial import simularHistorialPdf
from utils.registroVacunacion.simular_registro_vacunacion import simularRegistroVacunacion
from utils.usuarios.simular_usuarios import simular_usuarios
from utils.vacunasCatalogo.simular_vacunas_catalogo import simular_vacunas_catalogo

# Zona para importar limpiezas

from notebook.limpiar_alertas import limpiar_alertas
from notebook.limpiar_centros_medicos import limpiar_centros_medicos
from notebook.limpiar_historialPdf import limpiar_historial
from notebook.limpiar_registro_vacunacion import limpiar_registro_vacunacion
from notebook.limpiar_usuarios import limpiar_usuarios
from notebook.limpiar_vacunas_catalogo import limpiar_vacunas_catalogo


# Zona para importar descripciones

from notebook.describir_alertas import describir_alertas
from notebook.describir_centros_medicos import describir_centros_medicos
from notebook.describir_historialPdf import describir_historial
from notebook.describir_registro_vacunacion import describir_registro_vacunacion
from notebook.describir_usuarios import describir_usuarios
from notebook.describir_vacunas_catalogo import describir_vacunas_catalogo


# Creando las simulaciones

alertas_sim          = pd.DataFrame(simular_alertas(10))
centros_medicos_sim  = pd.DataFrame(simular_centros_medicos(10))
usuarios_sim         = pd.DataFrame(simular_usuarios(10))
vacunas_catalogo_sim = pd.DataFrame(simular_vacunas_catalogo())

ids_usuarios  = usuarios_sim["id_usuario"].tolist()
ids_centros   = centros_medicos_sim["id_centro"].tolist()
vacunas_lista = vacunas_catalogo_sim.to_dict("records")

historial_sim           = pd.DataFrame(simularHistorialPdf(10, ids_usuarios))
registro_vacunacion_sim = pd.DataFrame(
    simularRegistroVacunacion(10, ids_usuarios, vacunas_lista, ids_centros)
)


# Limpiando los sets de datos

alertas_limpias            = limpiar_alertas(alertas_sim)
centros_medicos_limpios    = limpiar_centros_medicos(centros_medicos_sim)
historial_limpio           = limpiar_historial(historial_sim)
registro_vacunacion_limpio = limpiar_registro_vacunacion(registro_vacunacion_sim)
usuarios_limpios           = limpiar_usuarios(usuarios_sim)
vacunas_catalogo_limpias   = limpiar_vacunas_catalogo(vacunas_catalogo_sim)


# Describiendo los sets de datos

describir_alertas(alertas_limpias)
describir_centros_medicos(centros_medicos_limpios)
describir_historial(historial_limpio)
describir_registro_vacunacion(registro_vacunacion_limpio)
describir_usuarios(usuarios_limpios)
describir_vacunas_catalogo(vacunas_catalogo_limpias)