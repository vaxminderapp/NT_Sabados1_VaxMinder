import pandas as pd


def limpiar_alertas(datos):
    df = pd.DataFrame(datos) if isinstance(datos, list) else datos.copy()

    print("Nulos detectados:")
    nulos_total = 0
    for col in df.columns:
        n = df[col].isna().sum()
        if n > 0:
            print(f"  {col}: {n}")
            nulos_total += n
    if nulos_total == 0:
        print("  (ninguno)")

    antes = len(df)
    df = df.drop_duplicates(subset=["id_alerta"], keep="first")

    tipos_validos   = ["refuerzo", "recordatorio", "vencimiento"]
    estados_validos = ["pendiente", "enviada", "leida", "descartada"]

    filas = []
    for _, f in df.iterrows():
        f = f.copy()

        if pd.isna(f["id_alerta"]) or int(f["id_alerta"]) <= 0:
            continue
        if pd.isna(f["id_usuario"]) or int(f["id_usuario"]) <= 0:
            continue
        if pd.isna(f["id_registro"]) or int(f["id_registro"]) <= 0:
            continue
        if f["tipo_alerta"] not in tipos_validos:
            continue
        if f["estado"] not in estados_validos:
            continue
        if pd.isna(f["fecha_alerta"]):
            continue
        if pd.isna(f["fecha_envio"]):
            continue
        if pd.isna(f["fecha_vencimiento"]):
            continue

        msg = str(f["mensaje"]).strip() if not pd.isna(f["mensaje"]) else ""
        if msg == "" or msg.upper() in ["N/A", "NONE", "NAN"]:
            continue

        f["id_alerta"]   = int(f["id_alerta"])
        f["id_usuario"]  = int(f["id_usuario"])
        f["id_registro"] = int(f["id_registro"])
        f["mensaje"]     = msg
        filas.append(f)

    resultado = pd.DataFrame(filas).reset_index(drop=True) if filas else df.iloc[0:0]
    print(f"\nResumen alertas: {antes} originales -> {antes - len(resultado)} eliminados -> {len(resultado)} validos\n")
    return resultado