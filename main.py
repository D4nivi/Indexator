import os
from funciones.indexators import indexator, quasi_indexator, re_indexator, menu
from funciones.indexators import set_subdivision, set_index, set_ignore_headers, set_no_index_headers
from funciones.presets import list_presets, add_preset, delete_preset, get_contents, get_preset

##### FUNCIONES AUXILIARES PARA EL PROGRAMA PRINCIPAL #####
def pause(msg: str = "") -> None:
    print(msg + "\n")
    print("Presione una tecla para continuar...", end="", flush=True)
    os.system("bash -c 'read -r -n 1 -s'")

def preset_indexation(n_preset: int = 0) -> None:
    set_subdivision(get_preset(n_preset)["subdivision"])
    set_index(get_preset(n_preset)["index"])
    set_ignore_headers(get_preset(n_preset)["ignore_headers"])
    set_no_index_headers(get_preset(n_preset)["no_index_headers"])
    re_indexator()

##### Programa principal #####
def main():
    opcion = ''

    while opcion != '0':
        try:
            menu()                      # Aquí se lee presets.json
            contents = get_contents()
            opcion = input()

            if opcion == '0':
                print("\nSaliendo...")
                exit(0)

            elif opcion == '1':
                indexator()
                pause("¡Terminado!")

            elif opcion == '2':
                quasi_indexator()
                pause("¡Terminado!")

            elif opcion == '3':
                re_indexator()
                pause("¡Terminado!")

            elif opcion == '4':
                set_ignore_headers(2)
                set_no_index_headers(2)
                re_indexator()
                pause("¡Terminado!")

            elif opcion == '5': set_subdivision()
            elif opcion == '6': set_index()
            elif opcion == '7': set_ignore_headers()
            elif opcion == '8': set_no_index_headers()
            elif opcion == '9':
                set_subdivision(False)
                set_index(1)
                set_ignore_headers(0)
                set_no_index_headers(0)

            elif opcion == '10' and len(contents) > 0:
                preset_indexation()
                pause("¡Terminado!")

            elif opcion == '11' and len(contents) > 1:
                list_presets()
                n_preset = -1

                while not 0 <= n_preset < len(contents):
                    try:
                        n_preset = int(input("Introduce el número de preset a usar: "))
                    except ValueError:
                        pass

                if n_preset != 0:
                    preset_indexation(n_preset)
                    pause("¡Terminado!")

            elif opcion == '12':
                if not add_preset():
                    pause("No se ha podido crear el preset.")

            elif opcion == '13' and len(contents) > 0:
                if not delete_preset():
                    pause("No se ha podido eliminar el preset")

            elif opcion == '14' and len(contents) > 0:
                list_presets()
                pause()

            else: pass

        except KeyboardInterrupt:
            pass
        except EOFError:
            print("\n\nAbortando...")
            exit(1)


if __name__ == "__main__":
    main()
