import pandas as pd


def limpiar_vacunas_catalogo(datos):
    df = pd.DataFrame(datos) if isinstance(datos, list) else datos.copy()

    antes = len(df)
    df = df.drop_duplicates(subset=["id_vacuna"], keep="first")
    df["id_vacuna"]         = df["id_vacuna"].astype(int)
    df["dosis_requeridas"]  = df["dosis_requeridas"].astype(int)

    print(f"Resumen catalogo: {antes} originales -> {len(df)} validos\n")
    return df.reset_index(drop=True)
