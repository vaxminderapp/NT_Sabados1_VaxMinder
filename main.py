import pandas as pd

# Zona para importar simulaciones
from utils.alertas.simular_alertas import simular_alertas
from utils.centros_medicos.simular_centros_medicos import simular_centros_medicos
from utils.historialPdf.simular_historial import simularHistorialPdf
from utils.registroVacunacion.simular_registro_vacunacion import simularRegistroVacunacion
from utils.usuarios.simular_usuarios import simular_usuarios
from utils.vacunasCatalogo.simular_vacunas_catalogo import simular_vacunas_catalogo

# Zona para importar transformaciones
from utils.alertas.transformar_alertas import transformar_alertas, consultar_alertas
from utils.centros_medicos.transformar_centros_medicos import transformar_centros_medicos, consultar_centros_medicos
from utils.usuarios.transformar_usuarios import transformar_usuarios, consultar_usuarios

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


# Simulando los datos
alertas_sim          = simular_alertas(30)
centros_medicos_sim  = simular_centros_medicos(30)
usuarios_sim         = simular_usuarios(30)
vacunas_catalogo_sim = pd.DataFrame(simular_vacunas_catalogo())

# Transformando los datos (inyectando errores)
alertas_transformadas         = transformar_alertas(alertas_sim)
centros_medicos_transformados = transformar_centros_medicos(centros_medicos_sim)
usuarios_transformados        = transformar_usuarios(usuarios_sim)

# Limpiando los sets de datos
alertas_limpias          = limpiar_alertas(alertas_transformadas)
centros_medicos_limpios  = limpiar_centros_medicos(centros_medicos_transformados)
usuarios_limpios         = limpiar_usuarios(usuarios_transformados)
vacunas_catalogo_limpias = limpiar_vacunas_catalogo(vacunas_catalogo_sim)

# Extraer IDs limpios para historial y registro de vacunación
ids_usuarios  = usuarios_limpios["id_usuario"].tolist()
ids_centros   = centros_medicos_limpios["id_centro"].tolist()
vacunas_lista = vacunas_catalogo_limpias.to_dict("records")

historial_sim           = pd.DataFrame(simularHistorialPdf(10, ids_usuarios))
registro_vacunacion_sim = pd.DataFrame(
    simularRegistroVacunacion(10, ids_usuarios, vacunas_lista, ids_centros)
)

historial_limpio           = limpiar_historial(historial_sim)
registro_vacunacion_limpio = limpiar_registro_vacunacion(registro_vacunacion_sim)


# Consultando los datos limpios con query()
consultar_alertas(alertas_limpias)
consultar_centros_medicos(centros_medicos_limpios)
consultar_usuarios(usuarios_limpios)


# Mostrando los datos limpios
print("\n========== DATOS LIMPIOS: ALERTAS ==========")
print(alertas_limpias.to_string())

print("\n========== DATOS LIMPIOS: CENTROS MÉDICOS ==========")
print(centros_medicos_limpios.to_string())

print("\n========== DATOS LIMPIOS: USUARIOS ==========")
print(usuarios_limpios.to_string())


# Describiendo los sets de datos
describir_alertas(alertas_limpias)
describir_centros_medicos(centros_medicos_limpios)
describir_historial(historial_limpio)
describir_registro_vacunacion(registro_vacunacion_limpio)
describir_usuarios(usuarios_limpios)
describir_vacunas_catalogo(vacunas_catalogo_limpias)
