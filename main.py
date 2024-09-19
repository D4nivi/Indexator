import os

RAW_PATH = os.path.join(os.getcwd(),"bruto.md")
INDEX_PATH = os.path.join(os.getcwd(),"indice.md")
TMP_PATH = os.path.join(os.getcwd(), "bruto_indexado.md")
INDEX = 1

# Si es True, añade INDEX al principio de cada numero del indice
SUBDIVISION = False

def indexator():
    with open(RAW_PATH, "r", encoding="utf-8") as infile, open(INDEX_PATH, "w", encoding="utf-8") as outfile, open(TMP_PATH, "w", encoding="utf-8") as tmpfile:
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


# Ídem al anterior pero lo uso cuando ya tengo los numeros en los titulos (o cuando no quiero poner numeros)
def quasi_indexator():
        with open(RAW_PATH, "r", encoding="utf-8") as infile, open(INDEX_PATH, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.startswith('#'):
                    hastags = line.count('#')
                    depth = hastags - 2

                    title = line[hastags+1:].rstrip()
                    format_title = title.replace(" ", "%20")

                    outfile.write(f"{'\t' * depth}- [{title}](#{format_title})\n")
            outfile.write("---\n")

opcion = ''

while(1):
    print("¿Qué vamos a usar hoy?\n(1) Indexator\n(2) Quasi-Indexator\n")
    print("(3) Alternar SUBDIVISION (valor = " + str(SUBDIVISION) + ")")
    print("(4) Cambiar INDEX (valor = " + str(INDEX) + ")\n")
    print("Opcion: ", end="")
    opcion = input()
    match opcion:
        case '1':
            indexator()
            print("¡Terminado!")
            break
        case '2':
            quasi_indexator()
            print("¡Terminado!")
            break
        case '3':
            SUBDIVISION = not SUBDIVISION
            print("SUBDIVISION = " + str(SUBDIVISION) + "\n")
        case '4':
            INDEX = int(input("Introduce el nuevo valor: "))
        case _: break

