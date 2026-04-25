import pandas as pd

# SIMULAR
from utils.alertas.simular_alertas import simular_alertas     
from utils.centros_medicos.simular_centros_medicos import simular_centros_medicos
from utils.usuarios.simular_usuarios import simular_usuarios

# TRANSFORMAR
from utils.alertas.transformar_alertas import transformar_alertas
from utils.centros_medicos.transformar_centros_medicos import transformar_centros_medicos
from utils.usuarios.transformar_usuarios import transformar_usuarios

# LIMPIAR
from utils.alertas.limpiar_alertas import limpiar_alertas
from utils.centros_medicos.limpiar_centros_medicos import limpiar_centros_medicos
from utils.usuarios.limpiar_usuarios import limpiar_usuarios


def mostrar_menu_principal():
    """Muestra el menú principal de opciones"""
    print("\n" + "="*60)
    print("       VAXMINDER - SISTEMA DE GESTIÓN DE VACUNACIÓN")
    print("="*60)
    print("\nOpciones principales:")
    print("1. Simular datos")
    print("2. Transformar datos")
    print("3. Limpiar datos")
    print("4. Salir")
    print("-"*60)
    return input("Selecciona una opción (1-4): ").strip()


def mostrar_menu_modulos():
    """Muestra el menú para seleccionar módulo"""
    print("\nMódulos disponibles:")
    print("1. Alertas")
    print("2. Centros Médicos")
    print("3. Usuarios")
    print("-"*60)
    return input("Selecciona un módulo (1-3): ").strip()


def simular():
    """Ejecuta la opción de simular datos"""
    print("\n--- SIMULAR DATOS ---")
    modulo = mostrar_menu_modulos()
    
    try:
        if modulo == "1":
            cantidad = int(input("¿Cuántas alertas deseas simular? "))
            datos = simular_alertas(cantidad)
            df = pd.DataFrame(datos) if isinstance(datos, list) else datos
            print(f"✓ Se simularon {cantidad} alertas")
            print(f"Primeras filas:\n{df.head()}")
            guardar = input("\n¿Deseas guardar los datos? (s/n): ").lower()
            if guardar == 's':
                df.to_csv("alertas_simuladas.csv", index=False)
                print("✓ Archivo guardado como 'alertas_simuladas.csv'")
                
        elif modulo == "2":
            cantidad = int(input("¿Cuántos centros médicos deseas simular? "))
            datos = simular_centros_medicos(cantidad)
            df = pd.DataFrame(datos) if isinstance(datos, list) else datos
            print(f"✓ Se simularon {cantidad} centros médicos")
            print(f"Primeras filas:\n{df.head()}")
            guardar = input("\n¿Deseas guardar los datos? (s/n): ").lower()
            if guardar == 's':
                df.to_csv("centros_medicos_simulados.csv", index=False)
                print("✓ Archivo guardado como 'centros_medicos_simulados.csv'")
                
        elif modulo == "3":
            cantidad = int(input("¿Cuántos usuarios deseas simular? "))
            datos = simular_usuarios(cantidad)
            df = pd.DataFrame(datos) if isinstance(datos, list) else datos
            print(f"✓ Se simularon {cantidad} usuarios")
            print(f"Primeras filas:\n{df.head()}")
            guardar = input("\n¿Deseas guardar los datos? (s/n): ").lower()
            if guardar == 's':
                df.to_csv("usuarios_simulados.csv", index=False)
                print("✓ Archivo guardado como 'usuarios_simulados.csv'")
        else:
            print("❌ Opción inválida")
    except ValueError:
        print("❌ Error: Debes ingresar un número válido")
    except Exception as e:
        print(f"❌ Error durante la simulación: {e}")


def transformar():
    """Ejecuta la opción de transformar datos"""
    print("\n--- TRANSFORMAR DATOS ---")
    modulo = mostrar_menu_modulos()
    
    try:
        archivo = input("Ingresa la ruta del archivo CSV a transformar: ").strip()
        df = pd.read_csv(archivo)
        
        if modulo == "1":
            datos = transformar_alertas(df.to_dict('records'))
            df_transformado = pd.DataFrame(datos) if isinstance(datos, list) else datos
            print(f"✓ Se transformaron {len(df_transformado)} registros de alertas")
            print(f"Primeras filas:\n{df_transformado.head()}")
            guardar = input("\n¿Deseas guardar los datos transformados? (s/n): ").lower()
            if guardar == 's':
                df_transformado.to_csv("alertas_transformadas.csv", index=False)
                print("✓ Archivo guardado como 'alertas_transformadas.csv'")
                
        elif modulo == "2":
            datos = transformar_centros_medicos(df.to_dict('records'))
            df_transformado = pd.DataFrame(datos) if isinstance(datos, list) else datos
            print(f"✓ Se transformaron {len(df_transformado)} registros de centros médicos")
            print(f"Primeras filas:\n{df_transformado.head()}")
            guardar = input("\n¿Deseas guardar los datos transformados? (s/n): ").lower()
            if guardar == 's':
                df_transformado.to_csv("centros_medicos_transformados.csv", index=False)
                print("✓ Archivo guardado como 'centros_medicos_transformados.csv'")
                
        elif modulo == "3":
            datos = transformar_usuarios(df.to_dict('records'))
            df_transformado = pd.DataFrame(datos) if isinstance(datos, list) else datos
            print(f"✓ Se transformaron {len(df_transformado)} registros de usuarios")
            print(f"Primeras filas:\n{df_transformado.head()}")
            guardar = input("\n¿Deseas guardar los datos transformados? (s/n): ").lower()
            if guardar == 's':
                df_transformado.to_csv("usuarios_transformados.csv", index=False)
                print("✓ Archivo guardado como 'usuarios_transformados.csv'")
        else:
            print("❌ Opción inválida")
    except FileNotFoundError:
        print("❌ Error: Archivo no encontrado")
    except Exception as e:
        print(f"❌ Error durante la transformación: {e}")


def limpiar():
    """Ejecuta la opción de limpiar datos"""
    print("\n--- LIMPIAR DATOS ---")
    modulo = mostrar_menu_modulos()
    
    try:
        archivo = input("Ingresa la ruta del archivo CSV a limpiar: ").strip()
        df = pd.read_csv(archivo)
        
        if modulo == "1":
            df_limpio = limpiar_alertas(df)
            print(f"✓ Se limpiaron {len(df_limpio)} registros de alertas")
            guardar = input("\n¿Deseas guardar los datos limpios? (s/n): ").lower()
            if guardar == 's':
                df_limpio.to_csv("alertas_limpias.csv", index=False)
                print("✓ Archivo guardado como 'alertas_limpias.csv'")
                
        elif modulo == "2":
            df_limpio = limpiar_centros_medicos(df)
            print(f"✓ Se limpiaron {len(df_limpio)} registros de centros médicos")
            guardar = input("\n¿Deseas guardar los datos limpios? (s/n): ").lower()
            if guardar == 's':
                df_limpio.to_csv("centros_medicos_limpios.csv", index=False)
                print("✓ Archivo guardado como 'centros_medicos_limpios.csv'")
                
        elif modulo == "3":
            df_limpio = limpiar_usuarios(df)
            print(f"✓ Se limpiaron {len(df_limpio)} registros de usuarios")
            guardar = input("\n¿Deseas guardar los datos limpios? (s/n): ").lower()
            if guardar == 's':
                df_limpio.to_csv("usuarios_limpios.csv", index=False)
                print("✓ Archivo guardado como 'usuarios_limpios.csv'")
        else:
            print("❌ Opción inválida")
    except FileNotFoundError:
        print("❌ Error: Archivo no encontrado")
    except Exception as e:
        print(f"❌ Error durante la limpieza: {e}")


def main():
    """Función principal - Menú interactivo"""
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            simular()
        elif opcion == "2":
            transformar()
        elif opcion == "3":
            limpiar()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()        
