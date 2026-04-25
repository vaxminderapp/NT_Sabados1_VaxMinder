from datetime import datetime, timedelta   
import random 

def simular_usuarios(numeroUsuarios):
    
    # Semillas de datos
    listaNombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", "Miguel", "Sofía", "Diego", "Valentina", 
                    "Andrés", "Camila", "Felipe", "Daniela", "Javier", "Isabel", "Ricardo", "Alejandra", "Manuel", "Catalina"]
    
    listaApellidos = ["García", "Rodríguez", "Martínez", "Pérez", "López", "Hernández", "Gómez", "Díaz", "Ramírez", "Cruz",
                      "Morales", "Castillo", "Vargas", "Rivas", "Fuentes", "Flores", "Soto", "Medina", "Delgado", "Vega"]
    
    listaTiposSangre = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    
    # Fechas
    fechaInicial = datetime(1960, 1, 1)
    fechaRegistroInicial = datetime(2026, 1, 1)
    
    usuarios = []
    cedulasUsadas = set()
    
    for _ in range(numeroUsuarios):
        # Generar cédula única (8-10 dígitos)
        while True:
            cedula = random.randint(10000000, 99999999)
            if cedula not in cedulasUsadas:
                cedulasUsadas.add(cedula)
                break
        
        # Datos básicos
        nombre = random.choice(listaNombres)
        apellido = random.choice(listaApellidos)
        
        # Email basado en nombre y apellido
        email = f"{nombre.lower()}.{apellido.lower()}{random.randint(1, 999)}@email.com"
        
        # Fecha de nacimiento (entre 1960 y 2010)
        diasAleatorios = random.randint(0, 18250)  # Aproximadamente 50 años
        fechaNacimiento = fechaInicial + timedelta(days=diasAleatorios)
        
        # Fecha de registro (durante el rango de 2026)
        diasRegistro = random.randint(0, 90)
        fechaRegistro = fechaRegistroInicial + timedelta(days=diasRegistro)
        
        # Teléfono colombiano simulado (10 dígitos)
        telefono = f"3{random.randint(10000000000, 99999999999)}"[:10]
        
        usuario = {
            "id_usuario": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "contraseña": "hashed_password_" + str(cedula),  # En producción sería bcrypt
            "fecha_nacimiento": fechaNacimiento.strftime("%Y-%m-%d"),
            "tipo_sangre": random.choice(listaTiposSangre),
            "telefono": telefono,
            "fecha_registro": fechaRegistro.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        usuarios.append(usuario)
    
    return usuarios


# Ejemplo de uso
if __name__ == "__main__":
    usuarios_simulados = simular_usuarios(10)
    for usuario in usuarios_simulados:
        print(usuario)
