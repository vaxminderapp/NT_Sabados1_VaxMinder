import pandas as pd


def describir_vacunas_catalogo(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: CATÁLOGO DE VACUNAS ==========")
    print(f"Total de vacunas en el catálogo: {df.shape[0]}")

    print("\n--- Listado completo de vacunas ---")
    print(f"  {'ID':>3}  {'Nombre':<20}  {'Dosis':<6}  {'Refuerzo':<9}  {'Descripción'}")
    print(f"  {'--':>3}  {'------':<20}  {'-----':<6}  {'--------':<9}  {'-----------'}")
    for _, fila in df.iterrows():
        refuerzo = "Sí" if fila['requiere_refuerzo'] else "No"
        print(f"  {int(fila['id_vacuna']):>3}  {fila['nombre_vacuna']:<20}  {int(fila['dosis_requeridas']):<6}  {refuerzo:<9}  {fila['descripcion']}")

    con_refuerzo = df['requiere_refuerzo'].sum()
    sin_refuerzo = len(df) - con_refuerzo
    print(f"\n--- Vacunas que requieren refuerzo ---")
    print(f"  Requieren refuerzo  : {con_refuerzo}")
    print(f"  No requieren refuerzo: {sin_refuerzo}")

    print(f"\n--- Distribución por número de dosis ---")
    for dosis, cantidad in df['dosis_requeridas'].value_counts().sort_index().items():
        print(f"  {dosis} dosis: {cantidad} vacuna(s)")
