import pandas as pd


def limpiar_registro_vacunacion(datos):
    df = pd.DataFrame(datos) if isinstance(datos, list) else datos.copy()

    print("Nulos detectados:")
    for col in df.columns:
        n = df[col].isna().sum()
        if n > 0:
            print(f"  {col}: {n}")

    antes = len(df)
    df = df.drop_duplicates(subset=["idRegistro"], keep="first")

    filas = []
    for _, f in df.iterrows():
        f = f.copy()
        if pd.isna(f["idRegistro"]) or int(f["idRegistro"]) <= 0:
            continue
        if pd.isna(f["idUsuario"]) or int(f["idUsuario"]) <= 0:
            continue
        if pd.isna(f["fechaAplicacion"]):
            continue
        dosis = f["numeroDosis"]
        if pd.isna(dosis) or int(dosis) <= 0 or int(dosis) > 10:
            continue
        lote = str(f["loteVacuna"]).strip() if not pd.isna(f["loteVacuna"]) else ""
        if len(lote) < 3 or lote.lower() in ["none", "nan"]:
            continue
        if pd.isna(f["idCentroMedico"]) or int(f["idCentroMedico"]) <= 0:
            continue
        f["idRegistro"]    = int(f["idRegistro"])
        f["idUsuario"]     = int(f["idUsuario"])
        f["idCentroMedico"] = int(f["idCentroMedico"])
        f["numeroDosis"]   = int(f["numeroDosis"])
        if pd.isna(f["observaciones"]) or str(f["observaciones"]).strip() == "":
            f["observaciones"] = None
        filas.append(f)

    resultado = pd.DataFrame(filas).reset_index(drop=True) if filas else df.iloc[0:0]
    print(f"\nResumen registro vacunacion: {antes} originales -> {antes - len(resultado)} eliminados -> {len(resultado)} validos\n")
    return resultado

