from storage import mensaje

def ver_historial_notas(datos, ident):
    print("\n=== Historial Académico del Camper ===")

    if ident not in datos["campers"]:
        mensaje("⚠️ Camper no encontrado.")
        return

    camper = datos["campers"][ident]
    print(f"\nNombre: {camper['nombres']} {camper['apellidos']}")
    print(f"Estado actual: {camper['estado']}")
    print(f"Riesgo académico: {camper['riesgo']}\n")

    if not camper["notas"]:
        mensaje("⚠️ No hay notas registradas para este camper.")
        return

    print("Módulo | Teoría | Práctica | Trabajos | Final | Estado")
    print("-" * 60)
    for modulo, info in camper["notas"].items():
        teoria = info.get("teoria", "-")
        practica = info.get("practica", "-")
        trabajos = info.get("trabajos", "-")
        final = info.get("final", "-")
        estado = info.get("estado", "-")
        print(f"{modulo:<15} {teoria:<8} {practica:<9} {trabajos:<10} {final:<7} {estado}")

    mensaje("Fin del historial.")

