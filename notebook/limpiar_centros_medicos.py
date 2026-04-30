import pandas as pd


def limpiar_centros_medicos(datos):
    df = pd.DataFrame(datos) if isinstance(datos, list) else datos.copy()

    print("Nulos detectados:")
    for col in df.columns:
        n = df[col].isna().sum()
        if n > 0:
            print(f"  {col}: {n}")

    antes = len(df)
    df = df.drop_duplicates(subset=["id_centro"], keep="first")

    filas = []
    for _, f in df.iterrows():
        f = f.copy()
        if pd.isna(f["id_centro"]) or int(f["id_centro"]) <= 0:
            continue
        nombre = str(f["nombre_centro"]).strip() if not pd.isna(f["nombre_centro"]) else ""
        if nombre == "" or nombre.lower() in ["none", "nan"]:
            continue
        if f["tipo_centro"] not in ["Hospital", "Clínica", "Centro de salud"]:
            continue
        tel = str(f["telefono"]).strip() if not pd.isna(f["telefono"]) else ""
        if len("".join(c for c in tel if c.isdigit())) < 7:
            continue
        # ciudad y direccion son obligatorios
        ciudad = str(f["ciudad"]).strip() if not pd.isna(f["ciudad"]) else ""
        if ciudad == "" or ciudad.lower() in ["none", "nan"]:
            continue
        direccion = str(f["direccion"]).strip() if not pd.isna(f["direccion"]) else ""
        if direccion == "" or direccion.lower() in ["none", "nan"]:
            continue
        f["nombre_centro"] = nombre
        f["ciudad"]        = ciudad.title()
        f["direccion"]     = direccion
        f["id_centro"]     = int(f["id_centro"])
        filas.append(f)

    resultado = pd.DataFrame(filas).reset_index(drop=True) if filas else df.iloc[0:0]
    print(f"\nResumen centros: {antes} originales -> {antes - len(resultado)} eliminados -> {len(resultado)} validos\n")
    return resultado