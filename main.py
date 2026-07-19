import os
import subprocess
import threading
from funciones.indexators import indexator, quasi_indexator, re_indexator, get_all, set_all, RAW_PATH, RAWINDEX_PATH
from funciones.indexators import set_use_wikilinks, set_subdivision, set_index, set_ignore_headers, set_no_index_headers
from funciones.presets import read_json, list_presets, add_preset, delete_preset, get_contents, get_preset, MAX_PRESETS
from funciones.menu import MenuItem, render_menu

# a nivel de módulo, junto a los imports
SUCCESS_MSG = f"\033[32mIndexación completada con éxito.\033[0m Copia el contenido de \033]8;;file://{RAWINDEX_PATH.replace(' ', '%20')}\a\033[1;4;35mbruto_indexado.md\033[0m\033]8;;\a."

##### FUNCIONES AUXILIARES PARA EL PROGRAMA PRINCIPAL #####
def pause(msg: str = "") -> None:
    """Función `"Pulse una tecla para continuar..."`."""

    print(msg + "\n")

    if os.name == "nt":
        os.system("pause")
    else:
        print("Presione una tecla para continuar...", end="", flush=True)
        os.system("read -r -n 1 -s")

def preset_indexation(n_preset: int = 0) -> None:
    """
    Función para indexar según los valores de las variables de un preset.
    
    Si no se especifica `n_preset`, se usa el primer preset de `presets.json`.
    """

    set_all(get_preset(n_preset))
    re_indexator()


def de_indexator(old_values: dict) -> None:
    """
    'De-Indexator': fuerza IGNORE_HEADERS y NO_INDEX_HEADERS a 2 para
    generar el documento sin numeración ni índice, y luego restaura
    los valores anteriores de configuración.
    """

    set_ignore_headers(2)
    set_no_index_headers(2)
    re_indexator()
    set_all(old_values)
    pause(SUCCESS_MSG)


def elegir_preset(old_values: dict, contents: list) -> None:
    """
    Pide al usuario que elija un preset por número, indexa con él,
    y restaura los valores anteriores de configuración.
    """

    list_presets()
    n_preset = -1

    while not 0 <= n_preset < len(contents):
        try:
            n_preset = int(input("Introduce el número de preset a usar: "))
        except ValueError:
            pass

    preset_indexation(n_preset)
    set_all(old_values)
    pause(SUCCESS_MSG)


def abrir_fichero(path: str):
    if os.name == 'nt':
        proc = subprocess.Popen(['start', '', path], shell=True)
    else:
        proc = subprocess.Popen(['xdg-open', path])

    proc.wait()


def abrir_en_hilo(path: str) -> None:
    """
    Abre un archivo con la aplicación predeterminada del sistema,
    en un hilo aparte para no bloquear el programa mientras se abre.
    """

    hilo = threading.Thread(target=abrir_fichero, args=(path,))
    hilo.start()

##### Programa principal #####
def build_menu_items(old_values: dict, contents: list) -> list[MenuItem]:
    variables = get_all()

    items = [
        MenuItem("¿Qué vamos a usar hoy?"),
        MenuItem("Indexator", lambda: indexator()),
        MenuItem("Quasi-Indexator", lambda: quasi_indexator()),
        MenuItem("Re-Indexator", lambda: re_indexator()),
        MenuItem("De-Indexator", lambda: de_indexator(old_values)),

        MenuItem(""),
        MenuItem("Configuración de variables"),
        MenuItem(f"Alternar USE_WIKILINKS (valor = {variables['use_wikilinks']})", set_use_wikilinks),
        MenuItem(f"Alternar SUBDIVISION (valor = {variables['subdivision']})", set_subdivision),
        MenuItem(f"Cambiar INDEX (valor = {variables['index']})", set_index),
        MenuItem(f"Cambiar IGNORE_HEADERS (valor = {variables['ignore_headers']})", set_ignore_headers),
        MenuItem(f"Cambiar NO_INDEX_HEADERS (valor = {variables['no_index_headers']})", set_no_index_headers),
        MenuItem("Restablecer a los valores predeterminados", lambda: set_all({
            "use_wikilinks": False, "subdivision": False, "index": 1,
            "ignore_headers": 0, "no_index_headers": 0
        })),

        MenuItem(""),
        MenuItem("Configuración de presets"),
    ]

    if read_json():
        if get_preset(0):
            items.append(MenuItem(
                f"Indexar con primer preset ('{get_preset(0)['name']}')",
                lambda: preset_indexation()
            ))
        if len(contents) > 1:
            items.append(MenuItem("Indexar con otro preset", elegir_preset))
        if len(contents) < MAX_PRESETS:
            items.append(MenuItem(
                f"Crear un preset ({len(contents)} preset(s) creado(s), MÁX. {MAX_PRESETS})",
                add_preset
            ))
        if len(contents) > 0:
            items.append(MenuItem("Eliminar un preset", delete_preset))
            items.append(MenuItem("Listar presets", lambda: (list_presets(), pause())))

    items += [
        MenuItem(""),
        MenuItem("Abrir archivos"),
        MenuItem("Abrir bruto.md", lambda: abrir_en_hilo(RAW_PATH), key="A"),
        MenuItem("Abrir bruto_indexado.md", lambda: abrir_en_hilo(RAWINDEX_PATH), key="B"),
    ]

    return items


def main():
    while True:
        old_values = get_all()
        contents = get_contents()
        dispatch = render_menu(build_menu_items(old_values, contents))

        try:
            opcion = input().strip().upper()
        except KeyboardInterrupt:
            continue
        except EOFError:
            print("\n\n\033[1;31mAbortando...\033[0m")
            exit(1)

        if opcion == "0":
            print("\nSaliendo...")
            exit(0)

        accion = dispatch.get(opcion)
        if accion: accion()


if __name__ == "__main__":
    open(RAW_PATH, "a").close()
    main()