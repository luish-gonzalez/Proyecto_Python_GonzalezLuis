from modules.storage import guardar_datos, mensaje

def registrar_nota_modulo(datos):
    print("\n=== Registrar Notas de Módulo ===")
    ident = input("ID del camper: ")

    if ident not in datos["campers"]:
        mensaje("⚠️ Camper no encontrado.")
        return

    camper = datos["campers"][ident]

    if camper["estado"] != "Cursando":
        mensaje(f"⚠️ El camper {camper['nombres']} no está cursando actualmente.")
        return

    modulo = input("Nombre del módulo evaluado: ")

    try:
        nota_teoria = float(input("Nota teórica (0-100): "))
        nota_practica = float(input("Nota práctica (0-100): "))
        nota_trabajos = float(input("Nota trabajos/quices (0-100): "))
    except ValueError:
        mensaje("❌ Ingrese valores numéricos válidos.")
        return

    
    camper["notas"][modulo] = {
        "teoria": nota_teoria,
        "practica": nota_practica,
        "trabajos": nota_trabajos
    }

    guardar_datos(datos)
    mensaje(f"✅ Notas del módulo '{modulo}' registradas para {camper['nombres']}.")

def calcular_nota_final_modulo(datos):
    print("\n=== Calcular Nota Final del Módulo ===")
    ident = input("ID del camper: ")

    if ident not in datos["campers"]:
        mensaje("⚠️ Camper no encontrado.")
        return

    camper = datos["campers"][ident]
    if not camper["notas"]:
        mensaje("⚠️ No hay módulos registrados para este camper.")
        return

    print("\nMódulos disponibles:")
    for mod in camper["notas"]:
        print(f"- {mod}")

    modulo = input("Ingrese el módulo para calcular nota final: ")
    if modulo not in camper["notas"]:
        mensaje("⚠️ Módulo no encontrado.")
        return

    n = camper["notas"][modulo]
    nota_final = (n["teoria"] * 0.3) + (n["practica"] * 0.6) + (n["trabajos"] * 0.1)
    camper["notas"][modulo]["final"] = round(nota_final, 2)

    if nota_final >= 60:
        camper["notas"][modulo]["estado"] = "Aprobado"
    else:
        camper["notas"][modulo]["estado"] = "Reprobado"

    guardar_datos(datos)
    mensaje(f"📊 Nota final del módulo '{modulo}': {nota_final:.2f} → {camper['notas'][modulo]['estado']}")

def marcar_riesgo(datos):
    print("\n=== Marcar Riesgo de Camper ===")
    ident = input("ID del camper: ")

    if ident not in datos["campers"]:
        mensaje("⚠️ Camper no encontrado.")
        return

    camper = datos["campers"][ident]

    if not camper["notas"]:
        mensaje("⚠️ Este camper no tiene módulos evaluados.")
        return

    
    notas_finales = []
    for modulo, info in camper["notas"].items():
        if "final" in info:
            notas_finales.append(info["final"])

    if not notas_finales:
        mensaje("⚠️ No hay notas finales calculadas para este camper.")
        return

    
    if any(n < 60 for n in notas_finales):
        camper["riesgo"] = "Alto"
    elif any(60 <= n < 70 for n in notas_finales):
        camper["riesgo"] = "Bajo"
    else:
        camper["riesgo"] = "Ninguno"

    guardar_datos(datos)
    mensaje(f"📋 Riesgo de {camper['nombres']} actualizado a: {camper['riesgo']}")

