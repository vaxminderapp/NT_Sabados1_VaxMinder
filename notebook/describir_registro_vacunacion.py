import pandas as pd
from utils.vacunasCatalogo.simular_vacunas_catalogo import simular_vacunas_catalogo


def describir_registro_vacunacion(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: REGISTRO DE VACUNACIÓN ==========")
    print(f"Total de vacunaciones registradas: {df.shape[0]}")

    if df.empty:
        print("  (no hay registros válidos para describir)")
        return

    # Cargar catálogo para cruzar nombres
    catalogo = pd.DataFrame(simular_vacunas_catalogo())[['id_vacuna', 'nombre_vacuna']]
    df_enriquecido = df.merge(catalogo, left_on='idVacuna', right_on='id_vacuna', how='left')

    print("\n--- Detalle de cada vacunación ---")
    print(f"  {'ID':>4}  {'ID Usuario':>12}  {'Vacuna':<22}  {'Dosis':<6}  {'Fecha Aplicación':<18}  {'Próxima Dosis'}")
    print(f"  {'--':>4}  {'----------':>12}  {'------':<22}  {'-----':<6}  {'----------------':<18}  {'-------------'}")
    for _, fila in df_enriquecido.iterrows():
        nombre_vacuna = fila['nombre_vacuna'] if pd.notna(fila.get('nombre_vacuna')) else f"ID {int(fila['idVacuna'])}"
        proxima = str(fila['proximaDosisfecha']) if pd.notna(fila['proximaDosisfecha']) else "No aplica"
        print(f"  {int(fila['idRegistro']):>4}  {int(fila['idUsuario']):>12}  {nombre_vacuna:<22}  {int(fila['numeroDosis']):<6}  {str(fila['fechaAplicacion']):<18}  {proxima}")

    print(f"\n--- Vacunas más aplicadas ---")
    for vacuna, cantidad in df_enriquecido.groupby('nombre_vacuna').size().sort_values(ascending=False).items():
        print(f"  {vacuna:<22}: {cantidad} aplicación(es)")

    print(f"\n--- Distribución por número de dosis ---")
    for dosis, cantidad in df['numeroDosis'].value_counts().sort_index().items():
        print(f"  Dosis {dosis}: {cantidad} registro(s)")

    pendientes_proxima = df['proximaDosisfecha'].notna().sum()
    print(f"\n--- Seguimiento de próximas dosis ---")
    print(f"  Pacientes con próxima dosis pendiente: {pendientes_proxima}")
    print(f"  Pacientes que completaron su esquema : {len(df) - pendientes_proxima}")

    print(f"\n--- Período de aplicación ---")
    print(f"  Vacunación más antigua : {df['fechaAplicacion'].min()}")
    print(f"  Vacunación más reciente: {df['fechaAplicacion'].max()}")