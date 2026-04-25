import random

from utils.usuarios.simular_usuarios import simular_usuarios


def transformar_usuarios(usuarios):
    usuarios_transformados = []

    for usuario in usuarios:
        # Copia el registro para no modificar el original
        usuario_transformado = usuario.copy()

        # Inyectando errores controlados
        probabilidadError = random.random()
        if probabilidadError < 0.1:
            # ID y nombre inválidos
            usuario_transformado["id_usuario"] = random.choice([None, -1, 0])
            usuario_transformado["nombre"] = random.choice(["", None, "   "])
        elif probabilidadError < 0.25:
            # Fechas nulas
            usuario_transformado["fecha_nacimiento"] = None
            usuario_transformado["fecha_registro"] = None
        elif probabilidadError < 0.4:
            # Email con formato inválido
            usuario_transformado["email"] = random.choice(["correo_sin_arroba", "@sinusuario.com", "", None])
        elif probabilidadError < 0.6:
            # Tipo de sangre inválido
            usuario_transformado["tipo_sangre"] = random.choice(["Z+", "XX", "", None, "desconocido"])
        elif probabilidadError < 0.8:
            # Teléfono con longitud incorrecta
            usuario_transformado["telefono"] = random.choice(["123", "abc1234567", "", None])
        else:
            # Apellido y contraseña vacíos
            usuario_transformado["apellido"] = random.choice(["", None, "   "])
            usuario_transformado["contraseña"] = random.choice(["", None])

        usuarios_transformados.append(usuario_transformado)

    return usuarios_transformados


if __name__ == "__main__":
    usuarios_simulados = simular_usuarios(5)
    print("Usuarios simulados:")
    print(usuarios_simulados)

    usuarios_transformados = transformar_usuarios(usuarios_simulados)
    print("\nUsuarios transformados (con errores inyectados):")
    print(usuarios_transformados)
