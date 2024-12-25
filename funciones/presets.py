import os
import json
import re

##### VARIABLES #####
CONTENTS = []
PRESETS_PATH = os.path.join(os.getcwd(), "presets.json")
MAX_PRESETS = 10


##### FUNCIONES #####
def read_json() -> bool:
    global CONTENTS

    try:
        jfile = open(PRESETS_PATH, "r")
        CONTENTS = json.load(jfile)

    except FileNotFoundError:
        print(f"Archivo 'presets.json' no encontrado en {os.getcwd()}.")
        CONTENTS = []

    except PermissionError:
        print(f"No se ha podido leer '{PRESETS_PATH}': Permiso denegado.")
        CONTENTS = []

    except json.JSONDecodeError:
        print(f"No se ha podido leer '{PRESETS_PATH}': Error de formato.")
        CONTENTS = []
    
    return CONTENTS != []

def list_presets() -> None:
    if len(CONTENTS) == 0:
        print("No hay presets para mostrar.")
    else:
        for preset in CONTENTS:
            print(f"Nombre: {preset['name']}")
            print(f"SUBDIVISION: {preset['subdivision']}")
            print(f"INDEX: {preset['index']}")
            print(f"IGNORE_HEADERS: {preset['ignore_headers']}")
            print(f"NO_INDEX_HEADERS: {preset['no_index_headers']}\n")

def create_preset() -> dict:
    taken_names = []
    name = ""

    # Obtener nombre
    for i in range(len(CONTENTS)):
        taken_names.append(CONTENTS[i]["name"])

    while not 0 < len(name) < 50 or name in taken_names:
        name = input("Introduce el nombre del preset (1-50 caracteres): ")

        if not 0 < len(name) < 50:
            print("Tamaño de nombre inválido.\n")

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
        "subdivision": entrada[1].lower(),
        "index": entrada[2],
        "ignore_headers": entrada[3],
        "no_index_headers": entrada[4]
    }

def add_preset() -> bool:
    # Comprobaciones
    if not os.path.exists(PRESETS_PATH):
        print("Archivo 'presets.json' no encontrado.")
        return False
        
    if len(CONTENTS) >= MAX_PRESETS:
        print("No se pueden crear más presets: máximo de presets alcanzado.")
        return False
        
    # Creación y añadido
    new_preset = create_preset()
    CONTENTS.append(new_preset)

    with open(PRESETS_PATH, "w") as jfile:
        json.dump(CONTENTS, jfile, indent=4)
    
    return True

def delete_preset(name: str) -> bool:
    # Comprobaciones
    if not os.path.exists(PRESETS_PATH):
        print(f"Archivo {PRESETS_PATH} no encontrado.")
        return False

    # Eliminado
    nuevos_presets = [preset for preset in CONTENTS if preset["name"] != name]

    if len(nuevos_presets) == len(CONTENTS):
        print(f"No se ha podido eliminar el preset '{name}': no existe un preset con ese nombre.")
        return False

    with open(PRESETS_PATH, "w") as jfile:
            json.dump(nuevos_presets, jfile, indent=4)
    
    return True

def get_contents() -> list:
    return CONTENTS