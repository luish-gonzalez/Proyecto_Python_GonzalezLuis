from storage import guardar_datos, mensaje
from models import crear_camper, crear_trainer, id_disponible, crear_ruta, crear_salon

def registrar_camper(datos):
    print("\n=== Registrar Camper ===")
    ident = input("ID del camper: ")

    if not id_disponible(datos, ident):
        return

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    acudiente = input("Acudiente: ")
    tel_cel = input("Teléfono celular: ")
    tel_fijo = input("Teléfono fijo: ")

    nuevo = crear_camper(ident, nombres, apellidos, direccion, acudiente, tel_cel, tel_fijo)
    datos["campers"][ident] = nuevo
    guardar_datos(datos)
    mensaje(f"✅ Camper {nombres} {apellidos} registrado correctamente.")
    
def registrar_trainer(datos):
    print("\n=== Registrar Trainer ===")
    ident = input("ID del trainer: ")

    if not id_disponible(datos, ident):
        return

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    especialidad = input("Especialidad principal: ")

    nuevo = crear_trainer(ident, nombres, apellidos, especialidad)
    datos["trainers"][ident] = nuevo
    guardar_datos(datos)
    mensaje(f"✅ Trainer {nombres} {apellidos} registrado correctamente.")

def crear_ruta_entrenamiento(datos):
    print("\n=== Crear Ruta de Entrenamiento ===")
    nombre = input("Nombre de la ruta (ej. Ruta NodeJS): ")

    # Validar que no exista otra ruta con el mismo nombre
    if nombre in datos["rutas"]:
        mensaje(f"⚠️ La ruta '{nombre}' ya existe.")
        return

    print("\nSeleccione los módulos para esta ruta:")
    modulos = {
        "Fundamentos de Programación": ["Introducción a la algoritmia", "PSeInt", "Python"],
        "Programación Web": ["HTML", "CSS", "Bootstrap"],
        "Programación Formal": ["Java", "JavaScript", "C#"],
        "Bases de Datos": ["Mysql", "MongoDb", "Postgresql"],
        "Backend": ["NetCore", "Spring Boot", "NodeJS", "Express"]
    }

    # Mostrar los módulos fijos
    for key in modulos:
        print(f"- {key}")

    nueva = crear_ruta(nombre, modulos)
    datos["rutas"][nombre] = nueva
    guardar_datos(datos)
    mensaje(f"✅ Ruta '{nombre}' creada correctamente.")

def crear_salon_entrenamiento(datos):
    print("\n=== Crear Salón de Entrenamiento ===")
    nombre = input("Nombre del salón (ej. Aula 1, Laboratorio A): ")

    if nombre in datos["salones"]:
        mensaje(f"⚠️ El salón '{nombre}' ya está registrado.")
        return

    nuevo = crear_salon(nombre)
    datos["salones"][nombre] = nuevo
    guardar_datos(datos)
    mensaje(f"✅ Salón '{nombre}' creado correctamente (capacidad: 33 campers).")

def registrar_examen_inicial(datos):
    print("\n=== Registrar Examen Inicial ===")
    ident = input("Ingrese el ID del camper: ")


    if ident not in datos["campers"]:
        mensaje(f"⚠️ El ID {ident} no está registrado como camper.")
        return

    camper = datos["campers"][ident]


    if camper["estado"] not in ["En proceso de ingreso", "Inscrito"]:
        mensaje(f"⚠️ El camper {camper['nombres']} no puede presentar examen (estado: {camper['estado']}).")
        return

    try:
        nota_teorica = float(input("Nota teórica (0-100): "))
        nota_practica = float(input("Nota práctica (0-100): "))
    except ValueError:
        mensaje("❌ Debe ingresar valores numéricos válidos.")
        return

    promedio = (nota_teorica + nota_practica) / 2


    if promedio >= 60:
        camper["estado"] = "Aprobado"
        camper["notas"]["examen_inicial"] = promedio
        mensaje(f"✅ Camper {camper['nombres']} aprobado con promedio {promedio:.2f}.")
    else:
        camper["estado"] = "No aprobado"
        camper["notas"]["examen_inicial"] = promedio
        mensaje(f"❌ Camper {camper['nombres']} NO aprobó (promedio {promedio:.2f}).")

    guardar_datos(datos)

def matricular_camper(datos):
    print("\n=== Matrícula de Camper ===")

    
    aprobados = [c for c in datos["campers"].values() if c["estado"] == "Aprobado"]
    if not aprobados:
        mensaje("⚠️ No hay campers aprobados para matricular.")
        return

    print("Campers aprobados disponibles:")
    for c in aprobados:
        print(f"- {c['id']} | {c['nombres']} {c['apellidos']}")

    ident = input("\nIngrese el ID del camper a matricular: ")

    if ident not in datos["campers"] or datos["campers"][ident]["estado"] != "Aprobado":
        mensaje("⚠️ ID inválido o camper no aprobado.")
        return

    camper = datos["campers"][ident]

    
    print("\nRutas disponibles:")
    for r in datos["rutas"]:
        print(f"- {r}")

    ruta_sel = input("Ingrese el nombre exacto de la ruta: ")
    if ruta_sel not in datos["rutas"]:
        mensaje("⚠️ Ruta no encontrada.")
        return

    ruta = datos["rutas"][ruta_sel]

    
    print("\nSalones disponibles:")
    for s, info in datos["salones"].items():
        cupos = 33 - len(info["campers"])
        print(f"- {s} (Cupos disponibles: {cupos})")

    salon_sel = input("Ingrese el nombre exacto del salón: ")
    if salon_sel not in datos["salones"]:
        mensaje("⚠️ Salón no encontrado.")
        return

    salon = datos["salones"][salon_sel]

    
    if len(salon["campers"]) >= salon["capacidad"]:
        mensaje("❌ Este salón está lleno. Elija otro.")
        return

    
    salon["campers"].append(ident)
    ruta["campers"].append(ident)
    camper["estado"] = "Cursando"
    camper["ruta_asignada"] = ruta_sel
    camper["salon"] = salon_sel

    guardar_datos(datos)
    mensaje(f"✅ Camper {camper['nombres']} matriculado en {ruta_sel} - {salon_sel}.")


