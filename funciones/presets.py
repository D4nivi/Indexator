import os
import json
import re

##### VARIABLES #####
CONTENTS = []
PRESETS_PATH = os.path.join(os.getcwd(), "presets.json")
MAX_PRESETS = 20


##### FUNCIONES #####
def read_json() -> bool:
    global CONTENTS

    if os.path.getsize(PRESETS_PATH) != 0:
        try:
            jfile = open(PRESETS_PATH, "r")
            CONTENTS = json.load(jfile)

        except FileNotFoundError:
            print(f"Archivo 'presets.json' no encontrado en {os.getcwd()}.")
            CONTENTS = None

        except PermissionError:
            print(f"No se ha podido leer '{PRESETS_PATH}': Permiso denegado.")
            CONTENTS = None

        except json.JSONDecodeError:
            print(f"No se ha podido leer '{PRESETS_PATH}': Error de formato.")
            CONTENTS = None
    
    return CONTENTS != None

def list_presets() -> None:
    print("\n----- Lista de presets -----")
    for i in range(len(CONTENTS)):
        print(f"({i}) Nombre: {CONTENTS[i]['name']}")
        print(f"\tSUBDIVISION: {CONTENTS[i]['subdivision']}")
        print(f"\tINDEX: {CONTENTS[i]['index']}")
        print(f"\tIGNORE_HEADERS: {CONTENTS[i]['ignore_headers']}")
        print(f"\tNO_INDEX_HEADERS: {CONTENTS[i]['no_index_headers']}\n")
        
def create_preset() -> dict:
    taken_names = []
    name = ""

    # Obtener nombre
    for i in range(len(CONTENTS)):
        taken_names.append(CONTENTS[i]["name"])

    while not 0 < len(name) < 20 or name in taken_names:
        name = input("Introduce el nombre del preset (1-20 caracteres): ")

        if len(name) > 20:
            print("Tamaño de nombre excedido.\n")

        if name in taken_names:
            print(f"El preset '{name}' ya existe. Por favor elige otro nombre.\n")

    # Obtener variables
    print("\nSUBDIVISION: True | False\nINDEX: >0\nIGNORE_HEADERS: (0|[2-6])\nNO_INDEX_HEADERS: (0|[2-6])\n")
    valores = input("Introduce los valores para las variables (Ejemplo: true 2 0 0): ").strip()
    entrada = re.fullmatch(r"(?i)(True|False)\ +(0|[1-9]\d*)\ +(0|[2-6])\ +(0|[2-6])", valores)

    while not entrada:
        print("Formato de entrada inválido.\n")
        valores = input("Introduce los valores para las variables: ").strip()
        entrada = re.fullmatch(r"(?i)(True|False)\ +([1-9]\d*)\ +(0|[2-6])\ +(0|[2-6])", valores)

    return {
        "name": name,
        "subdivision": entrada[1].lower() == "true",
        "index": int(entrada[2]),
        "ignore_headers": int(entrada[3]),
        "no_index_headers": int(entrada[4])
    }

def add_preset() -> bool:
    # Comprobaciones
    if not os.path.exists(PRESETS_PATH):
        print("Archivo '{PRESETS_PATH}' no encontrado.")
        return False
        
    if len(CONTENTS) >= MAX_PRESETS:
        print("Máximo de presets alcanzado.")
        return False

    # Creación y añadido
    new_preset = create_preset()
    CONTENTS.append(new_preset)

    with open(PRESETS_PATH, "w") as jfile:
        json.dump(CONTENTS, jfile, indent=4)

    return True

def delete_preset() -> bool:
    # Comprobaciones
    if not os.path.exists(PRESETS_PATH):
        print(f"Archivo '{PRESETS_PATH}' no encontrado.")
        return False

    # Eliminado
    for i in range(len(CONTENTS)):
        print(CONTENTS[i]["name"])

    name = input("\nEscribe el nombre del preset a eliminar: ")
    nuevos_presets = [preset for preset in CONTENTS if preset["name"] != name]

    if len(nuevos_presets) == len(CONTENTS):
        print(f"No existe el preset '{name}'.")
        return False

    with open(PRESETS_PATH, "w") as jfile:
        json.dump(nuevos_presets, jfile, indent=4)

    return True

def get_contents() -> list:
    return CONTENTS

def get_preset(n: int) -> str | list:
    return CONTENTS[n] if len(CONTENTS) > 0 else []