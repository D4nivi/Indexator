import os
from funciones.indexators import indexator, quasi_indexator, re_indexator, menu
from funciones.indexators import set_subdivision, set_index, set_ignore_headers, set_no_index_headers

##### FUNCIONES PARA EL PROGRAMA PRINCIPAL #####
def pause(msg: str) -> None:
    print(msg + "\n")
    print("Presione una tecla para continuar...", end="", flush=True)
    os.system("bash -c 'read -r -n 1 -s'")
    os.system("clear")


##### Programa principal #####
def main():
    opcion = ''

    while opcion != '0':
        menu()
        opcion = input()

        match opcion:
            case '0':
                print("\nSaliendo...")
                exit(0)

            case '1':
                indexator()
                pause("¡Terminado!")

            case '2':
                quasi_indexator()
                pause("¡Terminado!")

            case '3':
                re_indexator()
                pause("¡Terminado!")

            case '4':
                set_ignore_headers(2)
                set_no_index_headers(2)
                re_indexator()
                pause("¡Terminado!")

            case '5': set_subdivision()

            case '6': set_index()

            case '7': set_ignore_headers()

            case '8': set_no_index_headers()
            
            case '9':
                set_subdivision(False)
                set_index(1)
                set_ignore_headers(0)
                set_no_index_headers(0)

            case _: os.system("clear")

if __name__ == "__main__":
    main()
