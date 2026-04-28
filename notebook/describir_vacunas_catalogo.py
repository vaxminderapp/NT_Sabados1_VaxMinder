import pandas as pd


def describir_vacunas_catalogo(df: pd.DataFrame) -> None:
    print("\n========== DESCRIPCIÓN: VACUNAS CATÁLOGO ==========")
    print(f"Número de filas:      {df.shape[0]}")
    print(f"Número de columnas:   {df.shape[1]}")
    print(f"Columnas disponibles: {list(df.columns)}")

    stats = df[['id_vacuna', 'dosis_requeridas', 'intervalo_dosis_dias']].describe()
    stats['id_vacuna']           = stats['id_vacuna'].apply(lambda x: f"{int(x)}")
    stats['dosis_requeridas']    = stats['dosis_requeridas'].apply(lambda x: f"{int(round(x))}")
    stats['intervalo_dosis_dias']= stats['intervalo_dosis_dias'].apply(lambda x: f"{int(round(x))}")
    print(f"\nEstadísticas numéricas:\n{stats}")

    print(f"\nVacunas que requieren refuerzo:\n{df['requiere_refuerzo'].value_counts()}")
    print(f"\nDistribución por dosis requeridas:\n{df['dosis_requeridas'].value_counts().sort_index()}")
    print(f"\nValores nulos por columna:\n{df.isnull().sum().to_string()}")