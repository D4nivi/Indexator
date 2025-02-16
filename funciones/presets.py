import os
import json
import re

##### VARIABLES #####
CONTENTS = []
PRESETS_PATH = os.path.join(os.getcwd(), "presets.json")
MAX_PRESETS = 20
RE_CONF = re.compile(r"(?i)(?P<subdivision>(True|False|1|0)) +(?P<index>(0|[1-9]\d*)) +(?P<ignore_headers>(0|[2-6])) +(?P<no_index_headers>(0|[2-6]))")


##### FUNCIONES #####
def read_json() -> bool:
    """Lee el archivo `presets.json` y guarda sus contenidos en la variable `CONTENTS`."""
    
    global CONTENTS

    try:
        jfile = open(PRESETS_PATH, "r")

        # Si pongo esto fuera del try-except no comprueba los permisos si el archivo está vacío
        if os.path.getsize(PRESETS_PATH) != 0:
            CONTENTS = json.load(jfile)

    except FileNotFoundError:
        print(f"Archivo 'presets.json' no encontrado en {os.getcwd()}.")
        CONTENTS = None

    except PermissionError:
        print(f"No se ha podido acceder a '{PRESETS_PATH}': Permiso denegado.")
        CONTENTS = None

    except json.JSONDecodeError:
        print(f"No se ha podido leer '{PRESETS_PATH}': Error de formato.")
        CONTENTS = None
    
    return CONTENTS is not None

def list_presets() -> None:
    """
    Muestra los presets creados. Para cada uno, muestra:
    - Nombre del preset.
    - Valores de las variables (`SUBDIVISION`, `INDEX`, `IGNORE_HEADERS`, `NO_INDEX_HEADERS`).
    """

    print("\033[36m\n----- Lista de presets -----\033[0m")
    for i in range(len(CONTENTS)):
        print(f"({i}) Nombre: \033[34m{CONTENTS[i]['name']}\033[0m")
        print(f"\tSUBDIVISION: {CONTENTS[i]['subdivision']}")
        print(f"\tINDEX: {CONTENTS[i]['index']}")
        print(f"\tIGNORE_HEADERS: {CONTENTS[i]['ignore_headers']}")
        print(f"\tNO_INDEX_HEADERS: {CONTENTS[i]['no_index_headers']}\n")
        
def create_preset() -> dict:
    """
    Crea un preset. Para crear un preset, este debe:
    - Tener un nombre con 1-20 caracteres.
    - Tener un nombre que no esté usado.

    Devuelve un diccionario que contiene los datos del preset.
    """

    taken_names = []
    name = ""

    # Obtener nombre
    for i in range(len(CONTENTS)):
        taken_names.append(CONTENTS[i]["name"])

    while not 0 < len(name) < 20 or name in taken_names:
        name = input("Introduce el nombre del preset (1-20 caracteres): ").strip()

        if len(name) > 20:
            print("\033[33mTamaño de nombre excedido.\n\033[0m")

        if name in taken_names:
            print(f"\033[33mEl preset '{name}' ya existe. Por favor elige otro nombre.\n\033[0m")

    # Obtener variables
    print("\nSUBDIVISION: True | False | 1 | 0\nINDEX: >= 0\nIGNORE_HEADERS: (0|[2-6])\nNO_INDEX_HEADERS: (0|[2-6])\n")
    valores = input("Introduce los valores para las variables (Ejemplos: true 2 0 0 | 0 1 3 2): ").strip()
    entrada = RE_CONF.fullmatch(valores)

    while not entrada:
        print("\033[33mFormato de entrada inválido.\n\033[0m")
        valores = input("Introduce los valores para las variables: ").strip()
        entrada = RE_CONF.fullmatch(valores)

    return {
        "name": name,
        "subdivision": entrada["subdivision"].lower() == "true" or entrada["subdivision"] == "1",
        "index": int(entrada["index"]),
        "ignore_headers": int(entrada["ignore_headers"]),
        "no_index_headers": int(entrada["no_index_headers"])
    }

def add_preset() -> bool:
    """
    Añade un preset a `presets.json` si el número actual de presets no ha excedido `MAX_PRESETS`.

    Devuelve `True` si se pudo crear el preset.
    """

    # Comprobaciones
    if not os.path.exists(PRESETS_PATH):
        print("\033[31mArchivo '{PRESETS_PATH}' no encontrado.\033[0m")
        return False
        
    if len(CONTENTS) >= MAX_PRESETS:
        print("\033[31mMáximo de presets alcanzado.\033[0m")
        return False

    # Creación y añadido
    new_preset = create_preset()
    CONTENTS.append(new_preset)

    with open(PRESETS_PATH, "w") as jfile:
        json.dump(CONTENTS, jfile, indent=4)

    return True

def delete_preset() -> bool:
    """
    Elimina un preset dado su nombre. El nombre del preset tiene que existir y ser válido.

    Devuelve `True` si se pudo eliminar el preset.
    """
    
    # Comprobaciones
    if not os.path.exists(PRESETS_PATH):
        print(f"\033[31mArchivo '{PRESETS_PATH}' no encontrado.\033[0m")
        return False

    # Eliminado
    for i in range(len(CONTENTS)):
        print(CONTENTS[i]["name"])

    name = input("\nEscribe el nombre del preset a eliminar: ").strip()
    nuevos_presets = [preset for preset in CONTENTS if preset["name"] != name]

    if len(nuevos_presets) == len(CONTENTS):
        print(f"\033[31mNo existe el preset '{name}'.\033[0m")
        return False

    with open(PRESETS_PATH, "w") as jfile:
        json.dump(nuevos_presets, jfile, indent=4)

    return True

def get_contents() -> list:
    """Devuelve una copia del contenido de `presets.json`."""
    return CONTENTS

def get_preset(n: int) -> dict:
    """Devuelve un diccionario con los datos del preset `n`. Si no hay presets creados, devuelve un diccionario vacío."""
    return CONTENTS[n] if len(CONTENTS) > 0 else {}
