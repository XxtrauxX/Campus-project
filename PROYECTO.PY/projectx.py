import json
import hashlib
import os
import getpass
from datetime import datetime



# Funciones para manejar la contraseña
def encriptar_contraseña(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def verificar_contraseña(contrasena):
    try:
        with open("contraseña.json", "r") as f:
            data = json.load(f)
            return data["contraseña"] == encriptar_contraseña(contrasena)
    except FileNotFoundError:
        return False

def guardar_contraseña(contrasena):
    with open("contraseña.json", "w") as f:
        json.dump({"contraseña": encriptar_contraseña(contrasena)}, f)

# Función para cargar datos desde JSON
def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            return json.load(f)
    return []

# Función para guardar datos en JSON
def guardar_datos(archivo, datos):
    with open(archivo, "w") as f:
        json.dump(datos, f)

# Funciones de registro
def registrar_grupos(grupos):
    num_grupos = int(input("Ingrese el número de grupos a añadir: "))
    for _ in range(num_grupos):
        codigo = input("Ingrese el código del grupo: ")
        nombre = input("Ingrese el nombre del grupo: ")
        sigla = input("Ingrese la sigla del grupo: ")
        grupos.append({"codigo": codigo, "nombre": nombre, "sigla": sigla})
    guardar_datos("grupos.json", grupos)

def registrar_modulos(modulos):
    num_modulos = int(input("Ingrese el número de módulos a añadir: "))
    for _ in range(num_modulos):
        codigo = input("Ingrese el código del módulo: ")
        nombre = input("Ingrese el nombre del módulo: ")
        duracion = int(input("Ingrese la duración del módulo en semanas: "))
        modulos.append({"codigo": codigo, "nombre": nombre, "duracion": duracion})
    guardar_datos("modulos.json", modulos)

def registrar_estudiantes(estudiantes):
    num_estudiantes = int(input("Ingrese el número de estudiantes a añadir: "))
    for _ in range(num_estudiantes):
        codigo = input("Ingrese el código del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        sexo = input("Ingrese el sexo del estudiante (h/m): ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiantes.append({"codigo": codigo, "nombre": nombre, "sexo": sexo, "edad": edad})
    guardar_datos("estudiantes.json", estudiantes)

def registrar_docentes(docentes):
    num_docentes = int(input("Ingrese el número de docentes a añadir: "))
    for _ in range(num_docentes):
        cedula = input("Ingrese la cédula del docente: ")
        nombre = input("Ingrese el nombre del docente: ")
        docentes.append({"cedula": cedula, "nombre": nombre})
    guardar_datos("docentes.json", docentes)

# Registro de asistencia
def registrar_asistencia(asistencias):
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    codigo_modulo = input("Ingrese el código del módulo: ")
    hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hora_salida = input("Ingrese la hora de salida (dejar en blanco si no ha salido): ") or None
    asistencias.append({"codigo_estudiante": codigo_estudiante, "codigo_modulo": codigo_modulo, 
                        "hora_entrada": hora_entrada, "hora_salida": hora_salida})
    guardar_datos("asistencias.json", asistencias)

# Consultas
def consultar_estudiantes_por_grupo(grupos, estudiantes):
    grupo_consulta = input("Ingrese el código del grupo: ")
    estudiantes_en_grupo = [est for est in estudiantes if est.get('grupo') == grupo_consulta]
    if estudiantes_en_grupo:
        print(f"Estudiantes en el grupo {grupo_consulta}:")
        for est in estudiantes_en_grupo:
            print(f"- {est['nombre']} (Código: {est['codigo']})")
    else:
        print("No hay estudiantes en este grupo.")

# Función de menú
def menu():
    grupos = cargar_datos("grupos.json")
    modulos = cargar_datos("modulos.json")
    estudiantes = cargar_datos("estudiantes.json")
    docentes = cargar_datos("docentes.json")
    asistencias = cargar_datos("asistencias.json")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registro de grupos")
        print("2. Registro de módulos")
        print("3. Registro de estudiantes")
        print("4. Registro de docentes")
        print("5. Registro de asistencia")
        print("6. Consultas")
        print("7. Cambio de contraseña")
        print("8. Salida")

        eleccion = input("Seleccione una opción: ")
        if eleccion == "1":
            registrar_grupos(grupos)
        elif eleccion == "2":
            registrar_modulos(modulos)
        elif eleccion == "3":
            registrar_estudiantes(estudiantes)
        elif eleccion == "4":
            registrar_docentes(docentes)
        elif eleccion == "5":
            registrar_asistencia(asistencias)
        elif eleccion == "6":
            consultar_estudiantes_por_grupo(grupos, estudiantes)
        elif eleccion == "7":
            nueva_contrasena = getpass.getpass("Ingrese la nueva contraseña: ")
            guardar_contraseña(nueva_contrasena)
            print("Contraseña cambiada con éxito.")
        elif eleccion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función principal para iniciar el programa
def main():
    # Configuración inicial
    usu= input("ingrese el usuario\n")
    cont=input("Ingrese la contraseña:\n")


    if cont == "SISGESA":
        print(" ACCESO CONCEDIDO")

    else: 
        return
    menu()

if __name__ == "__main__":
    main()
