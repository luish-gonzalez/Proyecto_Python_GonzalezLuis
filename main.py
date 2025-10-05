import os
from storage import cargar_datos, guardar_datos, mensaje
from coordinador import registrar_camper, registrar_trainer, crear_ruta_entrenamiento, crear_salon_entrenamiento, registrar_examen_inicial, matricular_camper, asignar_trainer_a_ruta
from trainer import registrar_nota_modulo, calcular_nota_final_modulo, marcar_riesgo
from camper import ver_historial_notas
from reportes import listar_inscritos, listar_aprobados_inicial, listar_trainers, listar_bajo_rendimiento, listar_asociaciones, resumen_aprobados_reprobados




def login(datos):
    os.system("clear")
    print("=== LOGIN CAMPUSLAND ERP ===")
    ident = input("Ingrese su numero de identificación: ")

    if ident == "1096951955":
        print("Bienvenido coordinador")
        menu_coordinador()
        return
    
    if ident in datos["campers"]:
        print("Bienvenido Camper")
        menu_camper(datos, ident)
        return

    
    if ident in datos["trainers"]:
        print("Bienvenido Trainer")
        menu_trainer()
        return
    
    print("ID no encontrado. Revise su número e intente de nuevo.")

def menu_coordinador():
    while True:
        os.system("clear")
        print("=== MENÚ COORDINADOR ===")
        print("1. Registrar Camper")
        print("2. Registrar Trainer")
        print("3. Crear Ruta")
        print("4. Registrar Examen Inicial")
        print("5. Cambiar Estado de Camper")
        print("6. Asignar Trainer a Ruta")
        print("7. Matricular Camper")
        print("8. Reportes")
        print("9. Salir")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1": registrar_camper(datos)
            case "2": registrar_trainer(datos)
            case "3": crear_ruta_entrenamiento(datos)
            case "4": crear_salon_entrenamiento(datos)
            case "5": registrar_examen_inicial(datos)
            case "6": asignar_trainer_a_ruta(datos)
            case "7": matricular_camper(datos)
            case "8":
                print("\n=== REPORTES ===")
                print("1. Campers Inscritos")
                print("2. Campers Aprobados en Examen Inicial")
                print("3. Trainers Activos")
                print("4. Campers con Bajo Rendimiento")
                print("5. Asociaciones (Rutas ↔ Campers ↔ Trainers)")
                print("6. Resumen Aprobados/Reprobados por Módulo")
                opc_r = input("Seleccione un reporte: ")
                match opc_r:
                    case "1": listar_inscritos(datos)
                    case "2": listar_aprobados_inicial(datos)
                    case "3": listar_trainers(datos)
                    case "4": listar_bajo_rendimiento(datos)
                    case "5": listar_asociaciones(datos)
                    case "6": resumen_aprobados_reprobados(datos)
                    case _: mensaje("Opción inválida.")
            case "9": break
            case _: print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")

def menu_trainer():
    while True:
        os.system("clear")
        print("=== MENÚ TRAINER ===")
        print("1. Registrar Nota de Módulo")
        print("2. Calcular Nota Final")
        print("3. Marcar Riesgo")
        print("4. Salir")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1": registrar_nota_modulo(datos)
            case "2": calcular_nota_final_modulo(datos)
            case "3": marcar_riesgo(datos)
            case "4": break
            case _: print("Funcionalidad pendiente.")
        input("Presione Enter para continuar...")


def menu_camper(datos, ident):

    while True:
        os.system("clear")
        print("=== MENÚ CAMPER ===")
        print("1. Ver Historial de Notas")
        print("2. Salir")
        opc = input("Seleccione una opción: ")
        match opc:
            case "1": ver_historial_notas(datos, ident)
            case "2": break
            case _: print("Funcionalidad pendiente.")
        input("Presione Enter para continuar...")

if __name__ == "__main__":
    datos = cargar_datos()
    login(datos)
    guardar_datos(datos)