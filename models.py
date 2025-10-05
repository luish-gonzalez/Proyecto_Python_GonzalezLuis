from storage import mensaje

def crear_camper(ident, nombres, apellidos, direccion, acudiente, tel_cel, tel_fijo):
    return {
        "id": ident,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono_cel": tel_cel,
        "telefono_fijo": tel_fijo,
        "estado": "En proceso de ingreso",
        "riesgo": "Ninguno",
        "notas": {}
    }


def crear_trainer(ident, nombres, apellidos, especialidad):
    return {
        "id": ident,
        "nombres": nombres,
        "apellidos": apellidos,
        "especialidad": especialidad,
        "rutas_asignadas": []
    }

def id_disponible(datos, ident):
    if ident in datos["campers"] or ident in datos["trainers"]:
        mensaje(f"⚠️ El ID {ident} ya está registrado en el sistema.")
        return False
    return True

def crear_ruta(nombre, modulos):
    return {
        "nombre": nombre,
        "modulos": modulos,
        "campers": [],
        "trainers": []
    }


def crear_salon(nombre, capacidad=33):
    return {
        "nombre": nombre,
        "capacidad": capacidad,
        "campers": []
    }

