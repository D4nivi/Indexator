import os
import re
import fileinput

##### RUTAS A ARCHIVOS #####
# Path al bruto.md, de donde se lee el bruto a indexar.
RAW_PATH = os.path.join(os.getcwd(), "bruto.md")

# Path al archivo temporal .indice.md, donde se copiará el índice
INDEX_PATH = os.path.join(os.getcwd(), ".indice.md")

# Path al bruto_indexado.md, donde se copia el bruto indexado junto con el índice
RAWINDEX_PATH = os.path.join(os.getcwd(), "bruto_indexado.md")

# Path al archivo temporal .tmp.md, donde se copia el bruto sin los números de los encabezados ni índice
# Usado en función re_indexator()
TMP_PATH = os.path.join(os.getcwd(), ".tmp.md")


##### VARIABLES #####
USE_WIKILINKS = False
SUBDIVISION = False
INDEX = 1
IGNORE_HEADERS = 0
NO_INDEX_HEADERS = 0


##### FUNCIONES PRINCIPALES #####
def indexator(path = RAW_PATH) -> None:
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

        # Variable para detectar si el texto está entre backsticks (```)
        inside_backsticks = False

        heading_stack = []

        # Escritura
        tmpfile.write("# Índice de contenidos\n")
        for line in infile:
            subindex = ""

            if line.startswith("```") and not line.count("`") % 2 == 0:
                inside_backsticks = not inside_backsticks

            if line.startswith('##') and not inside_backsticks:
                # Cuento el número de hashtags
                hashtags = len(line) - len(line.lstrip('#'))

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

                # Calculamos primero el texto final del encabezado (el que realmente
                # quedará escrito en el archivo), porque ese es el texto que hay que
                # usar en la cadena de anidación, no el título "en bruto".
                if 0 < NO_INDEX_HEADERS <= hashtags:
                    heading_text = title
                elif SUBDIVISION:
                    heading_text = f"{INDEX}{subindex} {title}"
                else:
                    if depth == 0:
                        subindex = subindex[1:] + '.'
                    else:
                        subindex = subindex[1:]
                    heading_text = f"{subindex} {title}"

                # Pila de encabezados ancestros: reemplazamos el nivel actual y
                # truncamos todo lo que estuviera por debajo (igual que con subindexes)
                heading_stack = heading_stack[:depth] + [heading_text]

                tmpfile.write(build_index_link(depth, heading_text, heading_stack, USE_WIKILINKS))
                outfile.write(f"{'#' * hashtags} {heading_text}\n")

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
                hashtags = len(line) - len(line.lstrip('#'))
                depth = hashtags - 2

                title = line[hashtags+1:].rstrip()
                format_title = title.replace(" ", "%20")

                tmpfile.write(f"{'\t' * depth}- [{title}](#{format_title})\n")

            # Al final siempre escribo la misma línea del encabezado, ya que no se modifica
            outfile.write(line)
        
        tmpfile.write("---\n")

    add_index()
    os.remove(INDEX_PATH)
    

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


# Función para crear el enlace del encabezado (auxiliar)
def build_index_link(depth, heading_text, heading_stack, use_wikilinks):
    """Devuelve la línea de índice (con tabulación) para un encabezado dado."""
    if use_wikilinks:
        heading_path = "#".join(heading_stack)
        return f"{'\t' * depth}- [[#{heading_path}|{heading_text}]]\n"
    else:
        format_title = heading_text.replace(" ", "%20").replace(":", "")
        return f"{'\t' * depth}- [{heading_text}](#{format_title})\n"


# Función para borrar índice (auxiliar)
def del_index() -> None:
    tres_lineas = 0

    with open(RAW_PATH, "r", encoding="utf-8") as tmp:
        contenido = tmp.read()
    
    # Si hay índice, lo borramos. Se busca en los primeros 100 caracteres por si se encuentra la cadena en el documento.
    if contenido.find("# Índice de contenidos", 0, 100) != -1:
        for line in fileinput.input(RAW_PATH, inplace=True, encoding="utf-8"):

            # Cuando encontremos la primera ---, estaremos al principio del índice
            if line.startswith("---\n"):
                tres_lineas += 1

            # Mientras que estemos dentro del índice, tres_lineas = 1, luego no escribimos
            # Al terminar el índice, habrá otra ---, por lo que tres_lineas = 2 (escribiremos)
            if tres_lineas != 1:
                print(line, end='')

# Función para añadir índice (auxiliar)
def add_index() -> None:
    indice_copiado = False
    indice = ""

    # Guardamos el índice
    with open(INDEX_PATH, "r", encoding="utf-8") as tmp:
        # Ignoramos los encabezados hN si es necesario
        if IGNORE_HEADERS > 0:
            for line in tmp:
                if line.count("\t", 0, 4) < IGNORE_HEADERS - 2:
                    indice += line
        else:
            indice = tmp.read()

    for line in fileinput.input(RAWINDEX_PATH, inplace=True, encoding="utf-8"):
        # Cuando encontremos las ---, las imprimimos y copiamos el índice
        if not indice_copiado and line.startswith("---\n"):
            print(line, end='')
            print(indice, end='')
            indice_copiado = True
        else:
            # Copiamos todas las líneas al archivo
            print(line, end='')


##### SETTERS PARA EL MAIN #####
def set_use_wikilinks(value: bool | None = None) -> None:
    """
    Setter para variable USE_WIKILINKS.
    """

    global USE_WIKILINKS

    if value is None:
        USE_WIKILINKS = not USE_WIKILINKS
    else:
        USE_WIKILINKS = value

def set_subdivision(value: bool | None = None) -> None:
    """
    Setter para variable SUBDIVISION.

    - Si no se pasa un valor, este se pide por pantalla (usuario).
    - Si se pasa un valor, lo toma directamente (dev).
    """

    global SUBDIVISION

    if value is None:
        SUBDIVISION = not SUBDIVISION
    else:
        SUBDIVISION = value

def set_index(value: int | None = None) -> None:
    """
    Setter para variable INDEX.

    - Si no se pasa un valor, este se pide por pantalla (usuario).
    - Si se pasa un valor, lo toma directamente (dev).
    """

    global INDEX

    if value is None:
        value = -1
        while value < 0:
            try:
                value = int(input("Introduce el nuevo valor para INDEX (>= 0): "))
            except ValueError:
                pass

    INDEX = value

def set_ignore_headers(value: int | None = None) -> None:
    """
    Setter para variable IGNORE_HEADERS.

    - Si no se pasa un valor, este se pide por pantalla (usuario).
    - Si se pasa un valor, lo toma directamente (dev).
    """

    global IGNORE_HEADERS

    if value is None:
        value = -1
        while not (2 <= value <= 6 or value == 0):
            try:
                value = int(input("Introduce el nuevo valor para IGNORE_HEADERS (0|[2-6]): "))
            except ValueError:
                pass

    IGNORE_HEADERS = value

def set_no_index_headers(value: int | None = None) -> None:
    """
    Setter para variable NO_INDEX_HEADERS.

    - Si no se pasa un valor, este se pide por pantalla (usuario).
    - Si se pasa un valor, lo toma directamente (dev).
    """
    
    global NO_INDEX_HEADERS

    if value is None:
        value = -1
        while not (2 <= value <= 6 or value == 0):
            try:
                value = int(input("Introduce el nuevo valor para NO_INDEX_HEADERS (0|[2-6]): "))
            except ValueError:
                pass

    NO_INDEX_HEADERS = value

def get_all() -> dict:
    """Devuelve un diccionario con los valores de las variables del programa"""

    return {
        "use_wikilinks": USE_WIKILINKS,
        "subdivision": SUBDIVISION,
        "index": INDEX,
        "ignore_headers": IGNORE_HEADERS,
        "no_index_headers": NO_INDEX_HEADERS,
    }

def set_all(values: dict) -> None:
    """Función para cambiar el valor de todas las variables a la vez."""
    
    set_use_wikilinks(values["use_wikilinks"])
    set_subdivision(values["subdivision"])
    set_index(values["index"])
    set_ignore_headers(values["ignore_headers"])
    set_no_index_headers(values["no_index_headers"])