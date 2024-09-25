import os
import re
import fileinput

# Path al bruto.md, donde se pega el bruto a indexar
RAW_PATH = os.path.join(os.getcwd(),"bruto.md")

# Path al archivo temportal .indice.md, donde se copiará el índice
INDEX_PATH = os.path.join(os.getcwd(),".indice.md")

# Path al bruto_indexado.md, donde se copia el bruto indexado junto con el índice
RAWINDEX_PATH = os.path.join(os.getcwd(), "bruto_indexado.md")

# Path al archivo temporal .tmp.md, donde se copia el bruto sin los números de los encabezados ni índice
# Usado en función re_indexator()
TMP_PATH = os.path.join(os.getcwd(), ".tmp.md")

# Si SUBDIVISION es True, añade INDEX al principio de cada número del indice
# También es usado en re_indexator
SUBDIVISION = False
INDEX = 1

def indexator(path: str) -> None:
    with open(path, "r", encoding="utf-8") as infile, open(INDEX_PATH, "w", encoding="utf-8") as outfile, open(RAWINDEX_PATH, "w", encoding="utf-8") as tmpfile:
        # Lista con numero de subindice para cada nivel de profundidad (empezando con 0)
        # Verlo así: INDEX.0.0.0.0.0.0 (la profundidad tiene rango 0-5)
        subindexes = [0,0,0,0,0,0]

        # Numero de hastags anteriores, para comprobar si hemos bajado o subido en profundidad
        # Un indice (de los que hago yo) siempre empezará con un titulo con 2 hastags
        hastags_ant = 2

        # Escritura
        outfile.write("# Índice de contenidos\n")
        for line in infile:
            # Cadena del subindice
            subindex = ""

            if line.startswith('##'):
                # Cuento el número de hastags (no debería de haber en el titulo)
                hastags = line.count('#')
                

                # Profundidad del indice.
                # Ej.: 1.1 (2 hastags, depth 0), 1.1.1 (3 hastags, depth 1), y así
                depth = hastags - 2

                # Si subimos, reiniciamos los subindices dependiendo de cuantos niveles hayamos subido
                # P.e. si estabamos en profundidad 1 (INDEX.1.1.1) y subimos a la 0 (INDEX.1.1), debemos reiniciar
                # los indices de subindexes[2] en adelante 
                if hastags > hastags_ant:
                    subindexes[depth:] = [0] * (len(subindexes) - depth)

                # Cada vez que encontremos hastags, aumentamos el subindice según la profundidad
                subindexes[depth] += 1
                
                # El subindice será la combinación de los anteriores (si hay) + el nuevo
                for i in range(depth+1):
                    subindex += f".{subindexes[i]}"

                # Título (lo que va despues de los hastags, +1 porque hay un espacio)
                title = line[hastags+1:].rstrip()

                # Título formato markdown, sustituyendo espacios por %20
                format_title = title.replace(" ", "%20")

                # Escribo lineas del indice y cada titulo en bruto_indexado.md añadiendoles el numero
                if SUBDIVISION:
                    outfile.write(f"{'\t' * depth}- [{INDEX}{subindex} {title}](#{INDEX}{subindex}%20{format_title})\n")
                    tmpfile.write(f"{'#' * hastags} {INDEX}{subindex} {title}\n")
                else:
                    if depth == 0:
                        subindex = subindex[1:] + '.'
                    else:
                        subindex = subindex[1:]
                    outfile.write(f"{'\t' * depth}- [{subindex} {title}](#{subindex}%20{format_title})\n")
                    tmpfile.write(f"{'#' * hastags} {subindex} {title}\n")

                hastags_ant = hastags
            else:
                # Si la linea no tiene hastags, la ignoro y solo lo copio en el bruto_indexado.md
                tmpfile.write(line)
        
        # Toque final
        outfile.write("---\n")

    # Añadimos el índice al archivo y borramos .index.md
    add_index()
    os.remove(INDEX_PATH)


# Ídem al anterior pero lo uso cuando ya tengo los numeros en los titulos (o cuando no quiero poner numeros)
def quasi_indexator() -> None:
    with open(RAW_PATH, "r", encoding="utf-8") as infile, open(INDEX_PATH, "w", encoding="utf-8") as outfile:
        outfile.write("# Índice de contenidos\n")
        
        for line in infile:
            if line.startswith('##'):
                hastags = line.count('#')
                depth = hastags - 2

                title = line[hastags+1:].rstrip()
                format_title = title.replace(" ", "%20")

                outfile.write(f"{'\t' * depth}- [{title}](#{format_title})\n")
        
        outfile.write("---\n")


# Función para borrar índice (auxiliar)
def del_index() -> None:
    tres_lineas = 0

    with open(RAW_PATH, "r") as tmp:
        contenido = tmp.read()
    
    # Si hay indice, lo borramos
    if contenido.find("# Índice de contenidos") != -1:
        for line in fileinput.input(RAW_PATH, inplace=True):

            # Cuando encontremos la primera ---, estaremos al principio del indice
            if line.startswith("---\n"):
                tres_lineas += 1

            # Mientras que estemos dentro del indice, tres_lineas = 1, luego no escribimos
            # Al terminar el indice, habrá otra ---, por lo que tres_lineas = 2 (escribiremos)
            if tres_lineas != 1:
                print(line, end='')

# Función para añadir índice (auxiliar)
def add_index():
    indice_copiado = False

    # Guardamos el índice
    with open(INDEX_PATH, "r") as tmp:
        indice = tmp.read()

    for line in fileinput.input(RAWINDEX_PATH, inplace=True):
        # Cuando encontremos las ---, las imprimios y copiamos el indice
        if not indice_copiado and line.startswith("---\n"):
            print(line, end='')
            print(indice, end='')
            indice_copiado = True
        else:
            # Copiamos todas las lineas al archivo
            print(line, end='')


# Modifica el bruto para volver a crear un índice desde cero
def re_indexator() -> None:
    # Primero borramos el índice, ya que lo vamos a rehacer
    del_index()

    with open(RAW_PATH, "r", encoding="utf-8") as infile, open(TMP_PATH, "w", encoding="utf-8") as outfile:
        for line in infile:
            # Cambiamos los . por 0 para que sea más facil encontrar los encabezados en la re
            format_line = line.replace(".", "0")

            # Formatos de un encabezado
            hformat = re.match(r"^#{2,} [0-9]{2,} ", format_line)
            hformat2 = re.match(r"^#{2,} ", format_line)

            # Si se cumple el formato...
            if hformat != None or hformat2 != None:
                # Sacamos la longitud para quedarnos sólo con el título más adelante
                longitud = len(hformat.group()) if hformat != None else len(hformat2.group())

                hastags = line.count('#')

                title = line[longitud-1:]
                outfile.write(f"{"#"*hastags}{title}")

            else:
                outfile.write(line)

    indexator(TMP_PATH)
    os.remove(TMP_PATH)


# Programa principal
opcion = ''

while(1):
    print("¿Qué vamos a usar hoy?\n(1) Indexator\n(2) Quasi-Indexator\n(3) Re-Indexator\n")
    print("(4) Alternar SUBDIVISION (valor = " + str(SUBDIVISION) + ")")
    print("(5) Cambiar INDEX (valor = " + str(INDEX) + ")\n")
    print("Opcion: ", end="")
    opcion = input()
    match opcion:
        case '1':
            indexator(RAW_PATH)
            print("¡Terminado!")
            break
        case '2':
            quasi_indexator()
            print("¡Terminado!")
            break
        case '3':
            re_indexator()
            print("¡Terminado!")
            break
        case '4':
            SUBDIVISION = not SUBDIVISION
            print("SUBDIVISION = " + str(SUBDIVISION) + "\n")
        case '5':
            INDEX = int(input("Introduce el nuevo valor: "))
        case _: break

