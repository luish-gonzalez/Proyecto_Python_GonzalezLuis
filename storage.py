import json
import os

def cargar_datos():
    if not os.path.exists("campus.json"):
        datos = {
            "campers": {},
            "trainers": {},
            "rutas": {},
            "salones": {}
        }
        with open("campus.json", "w") as f:
            json.dump(datos, f, indent=4)
        return datos

    with open("campus.json", "r") as f:
        return json.load(f)
    
def guardar_datos(datos):
    with open("campus.json", "w") as f:
        json.dump(datos, f, indent=4)

def mensaje(texto):
    print(f"\n>>> {texto}")
    input("Presione Enter para continuar...")
