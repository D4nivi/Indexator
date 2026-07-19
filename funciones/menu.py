import os
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class MenuItem:
    """
    """
    label: str
    action: Optional[Callable[[], None]] = None   # None = línea decorativa (título de sección, etc.)
    key: Optional[str] = None                     # Para teclas fijas tipo "A"/"B"; si es None, se numera solo
    visible: bool = True
    show_success: bool = False

# Título sacado de https://patorjk.com/software/taag. Fuente: Big
TITULO = r"""  _____               _                         _                  
 |_   _|             | |                       | |                 
   | |    _ __     __| |   ___  __  __   __ _  | |_    ___    _ __ 
   | |   | '_ \   / _` |  / _ \ \ \/ /  / _` | | __|  / _ \  | '__|
  _| |_  | | | | | (_| | |  __/  >  <  | (_| | | |_  | (_) | | |   
 |_____| |_| |_|  \__,_|  \___| /_/\_\  \__,_|  \__|  \___/  |_|   
 """


def render_menu(items: list[MenuItem]) -> dict[str, MenuItem]:
    """
    Imprime el menú a partir de `items` y devuelve un diccionario
    {tecla: acción} para que el bucle principal despache directamente
    """

    os.system("cls" if os.name == "nt" else "clear")
    print(TITULO)

    dispatch = {}
    contador = 1

    for item in items:
        if not item.visible: continue

        if item.action is None:
            print(item.label)
            continue

        tecla = item.key or str(contador)
        print(f"({tecla}) {item.label}")
        dispatch[tecla] = item

        if item.key is None:
            contador += 1

    print("\n(0) Salir\n")
    print("Opción: ", end="")
    return dispatch