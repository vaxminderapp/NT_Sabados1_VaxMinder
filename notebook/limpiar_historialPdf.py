import pandas as pd


def limpiar_historial(datos):
    df = pd.DataFrame(datos) if isinstance(datos, list) else datos.copy()

    print("Nulos detectados:")
    for col in df.columns:
        n = df[col].isna().sum()
        if n > 0:
            print(f"  {col}: {n}")

    antes = len(df)
    df = df.drop_duplicates(subset=["idHistorial"], keep="first")

    rutas_invalidas = {"/ruta/invalida", "/storage/pdfs/usuarios/0/duplicado.pdf"}

    filas = []
    for _, f in df.iterrows():
        f = f.copy()
        if pd.isna(f["idHistorial"]) or int(f["idHistorial"]) <= 0:
            continue
        if pd.isna(f["idUsuario"]) or int(f["idUsuario"]) <= 0:
            continue
        if pd.isna(f["fechaGeneracion"]):
            continue
        nombre = str(f["nombreArchivo"]).strip() if not pd.isna(f["nombreArchivo"]) else ""
        if not nombre.endswith(".pdf") or nombre in ["", "none", "nan"]:
            continue
        ruta = str(f["rutaArchivo"]).strip() if not pd.isna(f["rutaArchivo"]) else ""
        if ruta == "" or ruta in rutas_invalidas:
            continue
        f["idHistorial"] = int(f["idHistorial"])
        f["idUsuario"]   = int(f["idUsuario"])
        filas.append(f)

    resultado = pd.DataFrame(filas).reset_index(drop=True) if filas else df.iloc[0:0]
    print(f"\nResumen historial: {antes} originales -> {antes - len(resultado)} eliminados -> {len(resultado)} validos\n")
    return resultado
