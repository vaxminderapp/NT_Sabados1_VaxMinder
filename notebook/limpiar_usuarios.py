import pandas as pd


def limpiar_usuarios(datos):
    df = pd.DataFrame(datos) if isinstance(datos, list) else datos.copy()

    print("Nulos detectados:")
    for col in df.columns:
        n = df[col].isna().sum()
        if n > 0:
            print(f"  {col}: {n}")

    antes = len(df)
    df = df.drop_duplicates(subset=["id_usuario"], keep="first")

    tipos_sangre = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]

    filas = []
    for _, f in df.iterrows():
        f = f.copy()
        if pd.isna(f["id_usuario"]) or int(f["id_usuario"]) <= 0:
            continue
        nombre = str(f["nombre"]).strip() if not pd.isna(f["nombre"]) else ""
        if nombre == "" or nombre.lower() in ["none", "nan"]:
            continue
        apellido = str(f["apellido"]).strip() if not pd.isna(f["apellido"]) else ""
        if apellido == "" or apellido.lower() in ["none", "nan"]:
            continue
        email = str(f["email"]).strip() if not pd.isna(f["email"]) else ""
        partes = email.split("@")
        if len(partes) != 2 or partes[0] == "" or "." not in partes[1]:
            continue
        clave = str(f["contraseña"]).strip() if not pd.isna(f["contraseña"]) else ""
        if clave == "" or clave.lower() in ["none", "nan"]:
            continue
        if pd.isna(f["fecha_nacimiento"]) or pd.isna(f["fecha_registro"]):
            continue
        if f["tipo_sangre"] not in tipos_sangre:
            continue
        tel = str(f["telefono"]).strip() if not pd.isna(f["telefono"]) else ""
        if any(c.isalpha() for c in tel):
            continue
        digitos = "".join(c for c in tel if c.isdigit())
        if len(digitos) < 7 or len(digitos) > 12:
            continue
        f["nombre"]   = nombre
        f["apellido"] = apellido
        f["email"]    = email
        f["id_usuario"] = int(f["id_usuario"])
        filas.append(f)

    resultado = pd.DataFrame(filas).reset_index(drop=True) if filas else df.iloc[0:0]
    print(f"\nResumen usuarios: {antes} originales -> {antes - len(resultado)} eliminados -> {len(resultado)} validos\n")
    return resultado
