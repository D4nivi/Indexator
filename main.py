import os
import re
import fileinput

##### RUTAS A ARCHIVOS #####
# Path al bruto.md, donde se pega el bruto a indexar.
RAW_PATH = os.path.join(os.getcwd(),"bruto.md")

# Path al archivo temporal .indice.md, donde se copiará el índice
INDEX_PATH = os.path.join(os.getcwd(),".indice.md")

# Path al bruto_indexado.md, donde se copia el bruto indexado junto con el índice
RAWINDEX_PATH = os.path.join(os.getcwd(), "bruto_indexado.md")

# Path al archivo temporal .tmp.md, donde se copia el bruto sin los números de los encabezados ni índice
# Usado en función re_indexator()
TMP_PATH = os.path.join(os.getcwd(), ".tmp.md")

##### VARIABLES #####
SUBDIVISION = False
"""
Si vale `True`, añade la variable `INDEX` al principio de cada número del índice.
"""

INDEX = 1
"""
Número de índice extra añadido a los títulos de los encabezados.

Solo se usa cuando `SUBDIVISION = False`.
"""

IGNORE_HEADERS = 0
"""
Indica a partir de que tamaño de encabezado no se pone en el índice.

Su valor por defecto es 0, lo que signfica que no se ignorará ninguno.

Ignora los encabezados `hN`, siendo `N` el valor de `IGNORE_HEADERS`.
"""

NO_INDEX_HEADERS = 0
"""
Indica a partir de que tamaño de encabezado no indexamos. Su valor puede ser `(0|[2-6])`.

Su valor por defecto es 0, lo que signfica que se indexan todos los encabezados.

No indexa los encabezados `hN`, siendo `N` el valor de `NO_INDEX_HEADERS`.
"""

##### FUNCIONES PRINCIPALES #####
def indexator(path: str) -> None:
    # infile: bruto.md (o .tmp.md si usamos re_indexator), archivo del que se lee.
    # outfile: bruto_indexado.md, donde se escribe el output del programa.
    # tmpfile: .indice.md, donde se escribe el índice para luego copiarlo en bruto_indexado.md.
    with open(path, "r", encoding="utf-8") as infile, open(RAWINDEX_PATH, "w", encoding="utf-8") as outfile, open(INDEX_PATH, "w", encoding="utf-8") as tmpfile:
        
        # Lista con número de subíndices para cada nivel de profundidad (empezando con 0)
        # Verlo así: INDEX.0.0.0.0.0.0 (la profundidad tiene rango 0-5)
        subindexes = [0,0,0,0,0,0]

        # Número de hashtags anteriores, para comprobar si hemos bajado o subido en profundidad
        # Un índice (de los que hago yo) siempre empezará con un titulo con 2 hashtags
        hashtags_ant = 2

        # Escritura
        tmpfile.write("# Índice de contenidos\n")
        for line in infile:
            # Cadena del subíndice
            subindex = ""

            if line.startswith('##'):
                # Cuento el número de hashtags (no debería de haber en el título)
                hashtags = line.count('#')

                # Profundidad del indice.
                # Ej.: 1.1 (2 hashtags, depth 0), 1.1.1 (3 hashtags, depth 1), y así
                depth = hashtags - 2

                # Si subimos, reiniciamos los subíndices dependiendo de cuantos niveles hayamos subido
                # P. ej. si estábamos en profundidad 1 (INDEX.1.1.1) y subimos a la 0 (INDEX.1.1), debemos reiniciar
                # los índices de subindexes[2] en adelante
                if hashtags > hashtags_ant:
                    subindexes[depth:] = [0] * (len(subindexes) - depth)

                # Cada vez que encontremos hashtags, aumentamos el subíndice según la profundidad
                subindexes[depth] += 1
                
                # El subíndice será la combinación de los anteriores (si hay) + el nuevo
                for i in range(depth+1):
                    subindex += f".{subindexes[i]}"

                # Título (lo que va después de los hashtags, +1 porque hay un espacio)
                title = line[hashtags+1:].rstrip()

                # Título formato markdown, sustituyendo espacios por %20
                format_title = title.replace(" ", "%20")

                # Escribo líneas del índice y cada título en bruto_indexado.md añadiéndoles el número
                if NO_INDEX_HEADERS > 0 and hashtags >= NO_INDEX_HEADERS:
                    tmpfile.write(f"{'\t' * depth}- [{title}](#{format_title})\n")
                    outfile.write(f"{'#' * hashtags} {title}\n")
                elif SUBDIVISION:
                    tmpfile.write(f"{'\t' * depth}- [{INDEX}{subindex} {title}](#{INDEX}{subindex}%20{format_title})\n")
                    outfile.write(f"{'#' * hashtags} {INDEX}{subindex} {title}\n")
                else:
                    if depth == 0:
                        subindex = subindex[1:] + '.'
                    else:
                        subindex = subindex[1:]
                    tmpfile.write(f"{'\t' * depth}- [{subindex} {title}](#{subindex}%20{format_title})\n")
                    outfile.write(f"{'#' * hashtags} {subindex} {title}\n")

                hashtags_ant = hashtags
            else:
                # Si la línea no tiene hashtags, la ignoro y solo lo copio en el bruto_indexado.md
                outfile.write(line)
        
        # Toque final
        tmpfile.write("---\n")

    # Añadimos el índice al archivo y borramos .index.md
    add_index()
    os.remove(INDEX_PATH)


# Ídem al anterior, pero lo uso cuando ya tengo los números en los títulos (o cuando no quiero poner números)
def quasi_indexator() -> None:
    with open(RAW_PATH, "r", encoding="utf-8") as infile, open(RAWINDEX_PATH, "w", encoding="utf-8") as outfile, open(INDEX_PATH, "w", encoding="utf-8") as tmpfile:
        tmpfile.write("# Índice de contenidos\n")
        
        for line in infile:
            if line.startswith('##'):
                hashtags = line.count('#')
                depth = hashtags - 2

                title = line[hashtags+1:].rstrip()
                format_title = title.replace(" ", "%20")

                tmpfile.write(f"{'\t' * depth}- [{title}](#{format_title})\n")

            # Al final siempre escribo la misma línea del encabezado, ya que no se modifica
            outfile.write(line)
        
        tmpfile.write("---\n")

    add_index()
    os.remove(INDEX_PATH)
    

# Función para borrar índice (auxiliar)
def del_index() -> None:
    tres_lineas = 0

    with open(RAW_PATH, "r") as tmp:
        contenido = tmp.read()
    
    # Si hay indice, lo borramos
    if contenido.find("# Índice de contenidos") != -1:
        for line in fileinput.input(RAW_PATH, inplace=True):

            # Cuando encontremos la primera ---, estaremos al principio del índice
            if line.startswith("---\n"):
                tres_lineas += 1

            # Mientras que estemos dentro del índice, tres_lineas = 1, luego no escribimos
            # Al terminar el índice, habrá otra ---, por lo que tres_lineas = 2 (escribiremos)
            if tres_lineas != 1:
                print(line, end='')

# Función para añadir índice (auxiliar)
def add_index():
    indice_copiado = False
    indice = ""

    # Guardamos el índice
    with open(INDEX_PATH, "r") as tmp:
        # Ignoramos los encabezados hN si es necesario
        if IGNORE_HEADERS > 0:
            for line in tmp:
                if line.count("\t", 0, 4) < IGNORE_HEADERS - 2:
                    indice += line
        else:
            indice = tmp.read()

    for line in fileinput.input(RAWINDEX_PATH, inplace=True):
        # Cuando encontremos las ---, las imprimimos y copiamos el índice
        if not indice_copiado and line.startswith("---\n"):
            print(line, end='')
            print(indice, end='')
            indice_copiado = True
        else:
            # Copiamos todas las líneas al archivo
            print(line, end='')


# Modifica el bruto para volver a crear un índice desde cero
def re_indexator() -> None:
    # Primero borramos el índice, ya que lo vamos a rehacer
    del_index()

    with open(RAW_PATH, "r", encoding="utf-8") as infile, open(TMP_PATH, "w", encoding="utf-8") as outfile:
        for line in infile:
            # Formatos de un encabezado
            # Formato 1: ## 1. |### 1.1 |#### 1.1.1 | ... (encabezado indexado)
            # Formato 2: ## |### |#### | ...              (encabezado sin indexar)
            hformat = re.match(r"^#{2,6} (\d+\.)+\d* ", line)
            hformat2 = re.match(r"^#{2,6} ", line)

            # Si se cumple el formato...
            if hformat is not None or hformat2 is not None:
                # Sacamos la longitud para quedarnos solo con el título más adelante
                longitud = len(hformat.group()) if hformat is not None else len(hformat2.group())

                hashtags = line.count('#')

                title = line[longitud-1:]
                outfile.write(f"{'#'*hashtags}{title}")

            else:
                outfile.write(line)

    indexator(TMP_PATH)
    os.remove(TMP_PATH)


##### FUNCIONES PARA EL PROGRAMA PRINCIPAL #####
def pause(msg: str):
    print(msg + "\n")
    print("Presione una tecla para continuar...", end="", flush=True)
    os.system("bash -c 'read -r -n 1 -s'")
    os.system("clear")

def menu():
    # Título sacado de https://patorjk.com/software/taag. Fuente: Big
    titulo = '''  _____               _                         _                  
 |_   _|             | |                       | |                 
   | |    _ __     __| |   ___  __  __   __ _  | |_    ___    _ __ 
   | |   | '_ \   / _` |  / _ \ \ \/ /  / _` | | __|  / _ \  | '__|
  _| |_  | | | | | (_| | |  __/  >  <  | (_| | | |_  | (_) | | |   
 |_____| |_| |_|  \__,_|  \___| /_/\_\  \__,_|  \__|  \___/  |_|   
 '''
    os.system("clear")
    print(titulo)
    print("¿Qué vamos a usar hoy?\n(1) Indexator\n(2) Quasi-Indexator\n(3) Re-Indexator\n(4) De-Indexator\n")
    print("(5) Alternar SUBDIVISION (valor = " + str(SUBDIVISION) + ")")
    print("(6) Cambiar INDEX (valor = " + str(INDEX) + ")")
    print("(7) Cambiar IGNORE_HEADERS (valor = " + str(IGNORE_HEADERS) + ")")
    print("(8) Cambiar NO_INDEX_HEADERS (valor = " + str(NO_INDEX_HEADERS) + ")\n")
    print("(9) Restablecer a los valores predeterminados\n(0) Salir\n")
    print("Opcion: ", end="")


##### Programa principal #####
if __name__ == "__main__":
    opcion = ''

    while opcion != '0':
        menu()
        opcion = input()

        match opcion:
            case '0':
                print("\nSaliendo...")
                exit(0)

            case '1':
                indexator(RAW_PATH)
                pause("¡Terminado!")

            case '2':
                quasi_indexator()
                pause("¡Terminado!")

            case '3':
                re_indexator()
                pause("¡Terminado!")

            case '4':
                IGNORE_HEADERS = 2
                NO_INDEX_HEADERS = 2
                re_indexator()
                pause("¡Terminado!")

            case '5':
                SUBDIVISION = not SUBDIVISION

            case '6':
                aux = int(input("Introduce el nuevo valor para INDEX (>= 0): "))
                if aux >= 0:
                    INDEX = aux

            case '7':
                aux = int(input("Introduce el nuevo valor para IGNORE_HEADERS (0|[2-6]): "))
                if aux == 0 or (2 <= aux <= 6):
                    IGNORE_HEADERS = aux

            case '8':
                aux = int(input("Introduce el nuevo valor para NO_INDEX_HEADERS (0|[2-6]): "))
                if aux == 0 or (2 <= aux <= 6):
                    NO_INDEX_HEADERS = aux
            
            case '9':
                SUBDIVISION = False
                INDEX = 1
                IGNORE_HEADERS = 0
                NO_INDEX_HEADERS = 0

            case _: os.system("clear")
