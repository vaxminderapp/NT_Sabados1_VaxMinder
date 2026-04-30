import pandas as pd

from utils.alertas.simular_alertas import simular_alertas
from utils.centros_medicos.simular_centros_medicos import simular_centros_medicos
from utils.historialPdf.simular_historial import simularHistorialPdf
from utils.registroVacunacion.simular_registro_vacunacion import simularRegistroVacunacion
from utils.usuarios.simular_usuarios import simular_usuarios
from utils.vacunasCatalogo.simular_vacunas_catalogo import simular_vacunas_catalogo

from utils.alertas.transformar_alertas import transformar_alertas
from utils.centros_medicos.transformar_centros_medicos import transformar_centros_medicos
from utils.historialPdf.transformar_historialpdf import transformar_historial
from utils.registroVacunacion.transformar_registro_vacunacion import transformar_registro_vacunacion
from utils.usuarios.transformar_usuarios import transformar_usuarios

from notebook.limpiar_alertas import limpiar_alertas
from notebook.limpiar_centros_medicos import limpiar_centros_medicos
from notebook.limpiar_historialPdf import limpiar_historial
from notebook.limpiar_registro_vacunacion import limpiar_registro_vacunacion
from notebook.limpiar_usuarios import limpiar_usuarios
from notebook.limpiar_vacunas_catalogo import limpiar_vacunas_catalogo

from notebook.describir_alertas import describir_alertas
from notebook.describir_centros_medicos import describir_centros_medicos
from notebook.describir_historialPdf import describir_historial
from notebook.describir_registro_vacunacion import describir_registro_vacunacion
from notebook.describir_usuarios import describir_usuarios
from notebook.describir_vacunas_catalogo import describir_vacunas_catalogo


def separador(titulo):
    print(f"\n{'='*65}")
    print(f"  {titulo}")
    print(f"{'='*65}")


def fila(valores, anchos):
    partes = []
    for v, a in zip(valores, anchos):
        texto = str(v) if v is not None else "(sin dato)"
        partes.append(texto[:a].ljust(a))
    return "  " + "  ".join(partes)


def tabla(titulo, columnas, anchos, filas_data):
    print(f"\n  {titulo}")
    print("  " + "-" * (sum(anchos) + 2 * len(anchos)))
    print(fila(columnas, anchos))
    print("  " + "-" * (sum(anchos) + 2 * len(anchos)))
    if not filas_data:
        print("  (sin registros validos)")
    else:
        for f_ in filas_data:
            print(fila(f_, anchos))
    print()


# ── 1. SIMULACIONES ──────────────────────────────────────
separador("PASO 1: SIMULACIONES")

alertas_sim          = simular_alertas(50)
centros_sim          = simular_centros_medicos(50)
usuarios_sim         = simular_usuarios(50)
vacunas_catalogo_sim = pd.DataFrame(simular_vacunas_catalogo())

print(f"  Alertas          : {len(alertas_sim)}")
print(f"  Centros medicos  : {len(centros_sim)}")
print(f"  Usuarios         : {len(usuarios_sim)}")
print(f"  Vacunas catalogo : {len(vacunas_catalogo_sim)}")


# ── 2. TRANSFORMACIONES ──────────────────────────────────
separador("PASO 2: TRANSFORMACIONES (inyeccion de errores)")

alertas_t  = transformar_alertas(alertas_sim)
centros_t  = transformar_centros_medicos(centros_sim)
usuarios_t = transformar_usuarios(usuarios_sim)

print(f"  Alertas transformadas  : {len(alertas_t)}")
print(f"  Centros transformados  : {len(centros_t)}")
print(f"  Usuarios transformados : {len(usuarios_t)}")


# ── 3. LIMPIEZAS ─────────────────────────────────────────
separador("PASO 3: LIMPIEZAS")

alertas_limpias          = limpiar_alertas(alertas_t)
centros_limpios          = limpiar_centros_medicos(centros_t)
usuarios_limpios         = limpiar_usuarios(usuarios_t)
vacunas_catalogo_limpias = limpiar_vacunas_catalogo(vacunas_catalogo_sim)

ids_usuarios  = usuarios_limpios["id_usuario"].tolist()
ids_centros   = centros_limpios["id_centro"].tolist()
vacunas_lista = vacunas_catalogo_limpias.to_dict("records")

historial_t = transformar_historial(simularHistorialPdf(15, ids_usuarios))
registro_t  = transformar_registro_vacunacion(
    simularRegistroVacunacion(15, ids_usuarios, vacunas_lista, ids_centros)
)

historial_limpio = limpiar_historial(pd.DataFrame(historial_t))
registro_limpio  = limpiar_registro_vacunacion(pd.DataFrame(registro_t))


# ── 4. DATOS LIMPIOS ─────────────────────────────────────
separador("PASO 4: DATOS LIMPIOS")

def val(x):
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return None
    if isinstance(x, float) and x == int(x):
        return int(x)
    if isinstance(x, str) and x.endswith(" 00:00:00"):
        return x.replace(" 00:00:00", "")
    return x

def preparar(df):
    rows = []
    for _, r in df.iterrows():
        rows.append([val(r[c]) for c in df.columns])
    return rows

# ALERTAS
print()
tabla(
    f"ALERTAS ({len(alertas_limpias)} registros)",
    ["ID", "ID Reg.", "ID Usuario", "Tipo", "Vencimiento", "Fecha Envio", "Estado"],
    [4, 7, 10, 12, 11, 11, 11],
    [[val(r["id_alerta"]), val(r["id_registro"]), val(r["id_usuario"]),
      r["tipo_alerta"], r["fecha_vencimiento"], r["fecha_envio"], r["estado"]]
     for _, r in alertas_limpias.iterrows()]
    if not alertas_limpias.empty else []
)

# CENTROS MEDICOS
tabla(
    f"CENTROS MEDICOS ({len(centros_limpios)} registros)",
    ["ID", "Nombre", "Tipo", "Ciudad", "Telefono"],
    [4, 30, 16, 15, 12],
    [[val(r["id_centro"]), r["nombre_centro"], r["tipo_centro"],
      r["ciudad"], r["telefono"]] for _, r in centros_limpios.iterrows()]
    if not centros_limpios.empty else []
)

# USUARIOS
tabla(
    f"USUARIOS ({len(usuarios_limpios)} registros)",
    ["Cedula", "Nombre", "Apellido", "Tipo Sangre", "Nacimiento", "Registro"],
    [10, 12, 12, 11, 10, 10],
    [[val(r["id_usuario"]), r["nombre"], r["apellido"],
      r["tipo_sangre"], r["fecha_nacimiento"],
      str(r["fecha_registro"]).replace(" 00:00:00", "")] for _, r in usuarios_limpios.iterrows()]
    if not usuarios_limpios.empty else []
)

# HISTORIAL PDF
tabla(
    f"HISTORIAL PDF ({len(historial_limpio)} registros)",
    ["ID", "ID Usuario", "Fecha", "Archivo"],
    [4, 10, 10, 55],
    [[val(r["idHistorial"]), val(r["idUsuario"]),
      str(r["fechaGeneracion"]).replace(" 00:00:00", ""), r["nombreArchivo"]]
     for _, r in historial_limpio.iterrows()]
    if not historial_limpio.empty else []
)

# REGISTRO VACUNACION
from utils.vacunasCatalogo.simular_vacunas_catalogo import simular_vacunas_catalogo as _cat
_catalogo = {v["id_vacuna"]: v["nombre_vacuna"] for v in _cat()}

tabla(
    f"REGISTRO VACUNACION ({len(registro_limpio)} registros)",
    ["ID", "ID Usuario", "Vacuna", "Dosis", "Fecha Aplicacion", "Prox. Dosis"],
    [4, 10, 20, 5, 16, 12],
    [[val(r["idRegistro"]), val(r["idUsuario"]),
      _catalogo.get(r["idVacuna"], f"ID {r['idVacuna']}"),
      val(r["numeroDosis"]), str(r["fechaAplicacion"]),
      str(r["proximaDosisfecha"]) if not pd.isna(r["proximaDosisfecha"]) else "No aplica"]
     for _, r in registro_limpio.iterrows()]
    if not registro_limpio.empty else []
)

# CATALOGO VACUNAS
tabla(
    f"CATALOGO DE VACUNAS ({len(vacunas_catalogo_limpias)} registros)",
    ["ID", "Nombre", "Dosis", "Refuerzo", "Descripcion"],
    [3, 18, 5, 8, 50],
    [[val(r["id_vacuna"]), r["nombre_vacuna"], val(r["dosis_requeridas"]),
      "Si" if r["requiere_refuerzo"] else "No", r["descripcion"]]
     for _, r in vacunas_catalogo_limpias.iterrows()]
)


# ── 5. DESCRIPCIONES ─────────────────────────────────────
separador("PASO 5: DESCRIPCIONES")

describir_alertas(alertas_limpias)
describir_centros_medicos(centros_limpios)
describir_usuarios(usuarios_limpios)
describir_historial(historial_limpio)
describir_registro_vacunacion(registro_limpio)
describir_vacunas_catalogo(vacunas_catalogo_limpias)
