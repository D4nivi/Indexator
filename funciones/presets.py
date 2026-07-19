import os
import json
import re
from dataclasses import dataclass
from typing import Callable, Any

##### ESQUEMA DE VARIABLES DE PRESET #####
@dataclass
class PresetField:
    key: str                      # Clave usada en el diccionario del preset (y en get_all/set_all)
    label: str                    # Nombre mostrado al usuario (list_presets, ayuda de create_preset)
    pattern: str                  # Regex (sin nombrar) que valida el valor en texto plano
    parser: Callable[[str], Any]  # Convierte el texto capturado al tipo real (bool, int...)
    hint: str                     # Descripción corta para la ayuda de create_preset
    default: Any = None           # Valor fallback para presets antiguos sin este campo

PRESET_FIELDS = [
    PresetField(
        key="use_wikilinks", label="USE_WIKILINKS",
        pattern=r"True|False|1|0",
        parser=lambda s: s.lower() in ("true", "1"),
        hint="USE_WIKILINKS: True | False | 1 | 0",
        default=False,
    ),
    PresetField(
        key="subdivision", label="SUBDIVISION",
        pattern=r"True|False|1|0",
        parser=lambda s: s.lower() in ("true", "1"),
        hint="SUBDIVISION: True | False | 1 | 0",
        default=False,
    ),
    PresetField(
        key="index", label="INDEX",
        pattern=r"0|[1-9]\d*",
        parser=int,
        hint="INDEX: >= 0",
        default=1,
    ),
    PresetField(
        key="ignore_headers", label="IGNORE_HEADERS",
        pattern=r"0|[2-6]",
        parser=int,
        hint="IGNORE_HEADERS: (0|[2-6])",
        default=0,
    ),
    PresetField(
        key="no_index_headers", label="NO_INDEX_HEADERS",
        pattern=r"0|[2-6]",
        parser=int,
        hint="NO_INDEX_HEADERS: (0|[2-6])",
        default=0,
    ),
]

# Regex construida dinámicamente a partir del esquema: un grupo nombrado por campo,
# unidos por espacios. Añadir un campo a PRESET_FIELDS ya actualiza esto solo.
RE_CONF = re.compile(
    r"(?i)" + r" +".join(f"(?P<{f.key}>{f.pattern})" for f in PRESET_FIELDS)
)


##### VARIABLES #####
CONTENTS = []
PRESETS_PATH = os.path.join(os.getcwd(), "presets.json")
MAX_PRESET_NAME = 40


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
    Muestra los presets creados en formato compacto: una línea por preset,
    con nombre y valores de todas las variables definidas en PRESET_FIELDS.
    Las variables que falten en el preset (JSON antiguo) se rellenan con su
    valor por defecto y se marcan con un asterisco.
    """

    print("\033[36m\n----- Lista de presets -----\033[0m")

    for i, preset in enumerate(CONTENTS):
        partes = []
        for field in PRESET_FIELDS:
            if field.key in preset:
                valor = preset[field.key]
                partes.append(f"{field.label}: {valor}")
            else:
                valor = field.default
                partes.append(f"\033[2m{field.label}: {valor}*\033[0m")

        linea_valores = " | ".join(partes)
        print(f"(\033[34m{i}\033[0m) \033[1m{preset['name']}\033[0m  —  {linea_valores}")

    print()


def create_preset() -> dict:
    """
    Crea un preset. Para crear un preset, este debe:
    - Tener un nombre con 1-MAX_PRESET_NAME caracteres.
    - Tener un nombre que no esté usado.

    Devuelve un diccionario que contiene los datos del preset.
    """

    taken_names = [preset["name"] for preset in CONTENTS]
    name = ""

    # Obtener nombre
    while not 0 < len(name) < MAX_PRESET_NAME or name in taken_names:
        name = input(f"Introduce el nombre del preset (1-{MAX_PRESET_NAME} caracteres): ").strip()

        if len(name) > MAX_PRESET_NAME:
            print("\033[33mTamaño de nombre excedido.\n\033[0m")

        if name in taken_names:
            print(f"\033[33mEl preset '{name}' ya existe. Por favor elige otro nombre.\n\033[0m")

    # Obtener variables
    ayuda = "\n".join(field.hint for field in PRESET_FIELDS)
    print(f"\n{ayuda}\n")

    valores = input(f"Introduce los valores para las variables en orden, separados por espacio: ").strip()
    entrada = RE_CONF.fullmatch(valores)

    while not entrada:
        print("\033[33mFormato de entrada inválido.\n\033[0m")
        valores = input("Introduce los valores para las variables: ").strip()
        entrada = RE_CONF.fullmatch(valores)

    preset = {"name": name}
    for field in PRESET_FIELDS:
        preset[field.key] = field.parser(entrada[field.key])

    return preset


def add_preset() -> bool:
    """
    Añade un preset a `presets.json` si el número actual de presets no ha excedido `MAX_PRESETS`.

    Devuelve `True` si se pudo crear el preset.
    """

    # Comprobaciones
    if not os.path.exists(PRESETS_PATH):
        print("\033[31mArchivo '{PRESETS_PATH}' no encontrado.\033[0m")
        return False

    # Creación y añadido
    new_preset = create_preset()
    CONTENTS.append(new_preset)

    with open(PRESETS_PATH, "w") as jfile:
        json.dump(CONTENTS, jfile, indent=4)

    return True


def delete_preset() -> bool:
    """
    Elimina un preset dado su número (el mismo que se muestra en list_presets).
    El número debe corresponder a un preset existente.

    Devuelve `True` si se pudo eliminar el preset.
    """

    if not os.path.exists(PRESETS_PATH):
        print(f"\033[31mArchivo '{PRESETS_PATH}' no encontrado.\033[0m")
        return False

    if len(CONTENTS) == 0:
        print("\033[31mNo hay presets para eliminar.\033[0m")
        return False

    list_presets()

    n_preset = -1
    while not 0 <= n_preset < len(CONTENTS):
        try:
            n_preset = int(input("Escribe el número del preset a eliminar: "))
        except ValueError:
            pass

    nombre = CONTENTS[n_preset]["name"]
    nuevos_presets = CONTENTS[:n_preset] + CONTENTS[n_preset + 1:]

    with open(PRESETS_PATH, "w") as jfile:
        json.dump(nuevos_presets, jfile, indent=4)

    print(f"\033[32mPreset '{nombre}' eliminado.\033[0m")
    return True

##### FUNCIONES AUXILIARES (USADAS EN OTROS MÓDULOS) #####
def fill_defaults(preset: dict) -> dict:
    """
    Devuelve una copia del preset con cualquier campo faltante rellenado con
    su valor por defecto.
    """
    return {
        field.key: preset.get(field.key, field.default)
        for field in PRESET_FIELDS
    }


def get_num_presets() -> int:
    """Devuelve el número de presets contenidos en `presets.json`."""
    return len(CONTENTS)


def get_preset(n: int) -> dict:
    """Devuelve un diccionario con los datos del preset `n`. Si no hay presets creados, devuelve un diccionario vacío."""
    return CONTENTS[n] if len(CONTENTS) > 0 else {}
