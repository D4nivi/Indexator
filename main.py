import os
import threading
import subprocess
from funciones.indexators import indexator, quasi_indexator, re_indexator, menu, get_all, RAW_PATH, RAWINDEX_PATH
from funciones.indexators import set_subdivision, set_index, set_ignore_headers, set_no_index_headers
from funciones.presets import list_presets, add_preset, delete_preset, get_contents, get_preset

##### FUNCIONES AUXILIARES PARA EL PROGRAMA PRINCIPAL #####
def pause(msg: str = "") -> None:
    """Función `"Pulse una tecla para continuar..."`."""

    print(msg + "\n")

    if os.name == "nt":
        os.system("pause")
    else:
        print("Presione una tecla para continuar...", end="", flush=True)
        os.system("read -r -n 1 -s")

def abrir_fichero(path: str):
    if os.name == 'nt':
        proc = subprocess.Popen(['start', '', path], shell=True)
    else:
        proc = subprocess.Popen(['xdg-open', path])

    proc.wait()

def set_all(values: list) -> None:
    """Función para cambiar el valor de todas las variables a la vez."""

    set_subdivision(values[0])
    set_index(values[1])
    set_ignore_headers(values[2])
    set_no_index_headers(values[3])

def preset_indexation(n_preset: int = 0) -> None:
    """
    Función para indexar según los valores de las variables de un preset.
    
    Si no se especifica `n_preset`, se usa el primer preset de `presets.json`.
    """
    
    set_all([
        get_preset(n_preset)["subdivision"],
        get_preset(n_preset)["index"],
        get_preset(n_preset)["ignore_headers"],
        get_preset(n_preset)["no_index_headers"]]
    )
    re_indexator()

##### Programa principal #####
def main():
    success_msg = f"\033[32mIndexación completada con éxito.\033[0m Copia el contenido de \033]8;;file://{RAWINDEX_PATH.replace(" ", "%20")}\a\033[1;4;35mbruto_indexado.md\033[0m\033]8;;\a."
    opcion = ''

    while opcion != '0':
        try:
            menu()                      # Aquí se lee presets.json
            contents = get_contents()
            old_values = get_all()
            opcion = input()

            if opcion == '0':
                print("\nSaliendo...")
                exit(0)

            elif opcion == '1':
                indexator()
                pause(success_msg)

            elif opcion == '2':
                quasi_indexator()
                pause(success_msg)

            elif opcion == '3':
                re_indexator()
                pause(success_msg)

            elif opcion == '4':
                set_ignore_headers(2)
                set_no_index_headers(2)
                re_indexator()
                set_all(old_values)
                pause(success_msg)

            elif opcion == '5': set_subdivision()
            elif opcion == '6': set_index()
            elif opcion == '7': set_ignore_headers()
            elif opcion == '8': set_no_index_headers()
            elif opcion == '9': set_all([False, 1, 0, 0])

            elif opcion == '10' and len(contents) > 0:
                preset_indexation()
                set_all(old_values)
                pause(success_msg)

            elif opcion == '11' and len(contents) > 1:
                list_presets()
                n_preset = -1

                while not 0 <= n_preset < len(contents):
                    try:
                        n_preset = int(input("Introduce el número de preset a usar: "))
                    except ValueError:
                        pass

                preset_indexation(n_preset)
                set_all(old_values)
                pause(success_msg)

            elif opcion == '12':
                if not add_preset():
                    pause("\033[31mNo se ha podido crear el preset.\033[0m")

            elif opcion == '13' and len(contents) > 0:
                if not delete_preset():
                    pause("\033[31mNo se ha podido eliminar el preset.\033[0m")

            elif opcion == '14' and len(contents) > 0:
                list_presets()
                pause()
            
            elif opcion.lower() == 'a':
                hilo = threading.Thread(target=abrir_fichero, args=(RAW_PATH,))
                hilo.start()

            elif opcion.lower() == 'b':
                hilo = threading.Thread(target=abrir_fichero, args=(RAWINDEX_PATH,))
                hilo.start()
                              
            else: pass

        except KeyboardInterrupt:
            pass
        except EOFError:
            print("\n\n\033[1;31mAbortando...\033[0m")
            exit(1)


if __name__ == "__main__":
    open(RAW_PATH, "a").close()
    main()