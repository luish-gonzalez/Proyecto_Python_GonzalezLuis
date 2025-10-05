from modules.storage import mensaje

def listar_inscritos(datos):
    print("\n=== Campers Inscritos ===")
    inscritos = [c for c in datos["campers"].values() if c["estado"] == "Inscrito"]
    if not inscritos:
        mensaje("⚠️ No hay campers inscritos actualmente.")
        return
    for c in inscritos:
        print(f"- {c['id']} | {c['nombres']} {c['apellidos']}")
    mensaje(f"Total inscritos: {len(inscritos)}")

def listar_aprobados_inicial(datos):
    print("\n=== Campers Aprobados en Examen Inicial ===")
    aprobados = [c for c in datos["campers"].values() if c["estado"] == "Aprobado"]
    if not aprobados:
        mensaje("⚠️ No hay campers aprobados.")
        return
    for c in aprobados:
        promedio = c["notas"].get("examen_inicial", "Sin registro")
        print(f"- {c['id']} | {c['nombres']} {c['apellidos']} | Promedio: {promedio}")
    mensaje(f"Total aprobados: {len(aprobados)}")

def listar_trainers(datos):
    print("\n=== Trainers Activos ===")
    if not datos["trainers"]:
        mensaje("⚠️ No hay trainers registrados.")
        return
    for t in datos["trainers"].values():
        rutas = ", ".join(t["rutas_asignadas"]) if t["rutas_asignadas"] else "Sin rutas asignadas"
        print(f"- {t['id']} | {t['nombres']} {t['apellidos']} | {rutas}")
    mensaje(f"Total trainers: {len(datos['trainers'])}")

def listar_bajo_rendimiento(datos):
    print("\n=== Campers con Bajo Rendimiento ===")
    riesgo = [c for c in datos["campers"].values() if c["riesgo"] in ["Bajo", "Alto"]]
    if not riesgo:
        mensaje("⚠️ No hay campers con bajo rendimiento.")
        return
    for c in riesgo:
        print(f"- {c['id']} | {c['nombres']} {c['apellidos']} | Riesgo: {c['riesgo']}")
    mensaje(f"Total en riesgo: {len(riesgo)}")

def listar_asociaciones(datos):
    print("\n=== Asociaciones de Rutas ===")
    if not datos["rutas"]:
        mensaje("⚠️ No hay rutas registradas.")
        return
    for nombre, ruta in datos["rutas"].items():
        print(f"\nRuta: {nombre}")
        print(f"Campers: {len(ruta['campers'])} | Trainers: {len(ruta['trainers'])}")
        if ruta["campers"]:
            print(" - Campers:")
            for cid in ruta["campers"]:
                c = datos["campers"].get(cid, {"nombres": "Desconocido", "apellidos": ""})
                print(f"   • {cid} | {c['nombres']} {c['apellidos']}")
        if ruta["trainers"]:
            print(" - Trainers:")
            for tid in ruta["trainers"]:
                t = datos["trainers"].get(tid, {"nombres": "Desconocido", "apellidos": ""})
                print(f"   • {tid} | {t['nombres']} {t['apellidos']}")
    mensaje("Fin del listado de asociaciones.")

def resumen_aprobados_reprobados(datos):
    print("\n=== Resumen de Aprobados y Reprobados por Módulo ===")
    conteo = {}
    for camper in datos["campers"].values():
        for modulo, info in camper["notas"].items():
            if "estado" in info:
                conteo.setdefault(modulo, {"Aprobado": 0, "Reprobado": 0})
                conteo[modulo][info["estado"]] += 1

    if not conteo:
        mensaje("⚠️ No hay módulos evaluados aún.")
        return

    print("Módulo | Aprobados | Reprobados")
    print("-" * 35)
    for modulo, valores in conteo.items():
        print(f"{modulo:<15} {valores['Aprobado']:<10} {valores['Reprobado']}")
    mensaje("Fin del resumen.")

