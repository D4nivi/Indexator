# Indexator

Indexator es un programa simple de Python que crea **índices Markdown**. Está pensado para ser usado en ***Obsidian***, y funciona tanto en Windows como en Linux.

Es un programa hecho a mis gustos y a mi manera de organizar los apartados, por lo que la estructura puede no ser como te gustaría (en cuyo caso, siéntete libre de modificar el programa a tu gusto).

## Índice de contenidos
- [Requisitos](#Requisitos)
- [¿Cómo funciona Indexator?](#cómo-funciona-indexator)
- [Cómo usar](#cómo-usar)
- [Funciones](#Funciones)
- [Variables](#Variables)
	- [Notas sobre las variables](#notas-sobre-las-variables)
- [Presets](#Presets)
- [Notas Importantes](#notas-importantes)

## Requisitos
Python 3.8 o superior: Puedes ver tu versión de Python con `python --version` o `python3 --version`.

## ¿Cómo funciona Indexator?
Imaginemos que tenemos una nota de Obsidian con el siguiente esquema (supongamos que entre los encabezados hay texto):

```
## Definición de rendimiento
## Métricas populares
### Tiempo de ejecución
### Otras métricas de rendimiento
## Ley de Amdahl
## Cómo comparar resultados
## Programas de Prueba (Benchmarks)
```
Un índice se creará a partir de los encabezados Markdown (las almohadillas #). Dependiendo del número de almohadillas, el programa detecta y crea un subíndice. La transformación que hace el programa es la siguiente:
```
## -> 1.
### -> 1.1
#### -> 1.1.2
#### -> 1.1.2.3
##### -> 1.1.2.3.4
###### -> 1.1.2.3.4.5
```
- ___Nota: los números son orientativos, en un caso real como este todos los números serían unos.___

Si le pasamos al programa el contenido anterior, podría indexarlo de esta manera:
```
## 1. Definición de rendimiento
## 2. Métricas populares
### 2.1 Tiempo de ejecución
### 2.2 Otras métricas de rendimiento
## 3. Ley de Amdahl
## 4. Cómo comparar resultados
## 5. Programas de Prueba (Benchmarks)
```

**El índice solo se creará cuando se detecten "---"**. Esto se hace así para evitar que el índice se escriba siempre al principio de la nota, y puedas controlar dónde ponerlo. Es decir, el ejemplo anterior no creará un índice, a no ser que pongamos "---" antes del primer encabezado:
```
---
## Definición de rendimiento
## Métricas populares
### Tiempo de ejecución
### Otras métricas de rendimiento
## Ley de Amdahl
## Cómo comparar resultados
## Programas de Prueba (Benchmarks)
```

Si le pasamos al programa el contenido anterior, podría indexarlo de esta manera:
```
---
# Índice de contenidos
- [1. Definición de rendimiento](#1.%20Definición%20de%20rendimiento)
- [2. Métricas populares](#2.%20Métricas%20populares)
	- [2.1 Tiempo de ejecución](#2.1%20Tiempo%20de%20ejecución)
	- [2.2 Otras métricas de rendimiento](#2.2%20Otras%20métricas%20de%20rendimiento)
- [3. Ley de Amdahl](#3.%20Ley%20de%20Amdahl)
- [4. Cómo comparar resultados](#4.%20Cómo%20comparar%20resultados)
- [5. Programas de Prueba (Benchmarks)](#5.%20Programas%20de%20Prueba%20(Benchmarks))
---
## 1. Definición de rendimiento
## 2. Métricas populares
### 2.1 Tiempo de ejecución
### 2.2 Otras métricas de rendimiento
## 3. Ley de Amdahl
## 4. Cómo comparar resultados
## 5. Programas de Prueba (Benchmarks)
```

Nótese que el índice queda encerrado entre "---". Esto es crucial para detectarlo y poder usar funciones como `Re-Indexator` o `De-Indexator`. En el apartado _[Funciones](#funciones)_, puedes ver un ejemplo de cómo se vería este índice en Obsidian.

## Cómo usar
Para indexar una nota de Obsidian, primero debemos copiar el contenido de la nota al archivo `bruto.md` de la carpeta del proyecto. No es necesario copiar solamente los encabezados, podemos copiar el texto completo (incluidas etiquetas e índice, en el caso de que hubiera). Abrimos una terminal en dicha carpeta y ejecutamos el programa:
```python
python main.py
```
Al ejecutar el programa <strong>por <u>primera vez</u></strong> nos aparecerá un **menú** como el siguiente:

<div align="center">
    <img src="img/Menú indexator primera ejecución.png" width="70%" alt="Ejemplo salida indexator">
</div>

En este menú podemos seleccionar la **función que queramos usar para indexar** (ver [_Funciones_](#Funciones)). El archivo `bruto_indexado.md` contendrá la salida del programa: **el bruto con los encabezados modificados** (con los números añadidos) y **el índice** pegado al principio de la nota.

En la <u><strong>Configuracion de variables</strong></u> podemos **cambiar los valores de algunas variables** para modificar el formato del indexado y el índice. Estas variables se explican en el apartado [_Variables_](#variables).

En la <u><strong>Configuracion de presets</strong></u> tenemos solo una opción, para crear **presets**. Si pretendes usar varias veces una misma configuración de variables (que no sea la predeterminada), puedes **guardarlas en un preset** y usarlo para indexar sin tener que cambiar los valores de las variables manualmente (ver _[Presets](#Presets)_). 

Cuando crees presets, aparecerán más opciones en el menú:

<div align="center">
    <img src="img/Menú indexator tras crear 2 presets.png" width="70%" alt="Ejemplo salida indexator">
</div>

- Para indexar con el primer preset que hayas creado, usas la opción (10). Esta opción siempre usará el primer preset.
- Si creas más presets, puedes usarlos con la opción (11).
- La opción (14) muestra los nombres y valores de las variables para todos los presets.
- Para cancelar cualquier operación en curso, puedes usar `Ctrl+C`. Para salir forzosamente del programa, usa `Ctrl+D` (solo disponible en Linux).

## Funciones
***Antes de usar cualquiera de las siguientes funciones***, ver [Notas Importantes](#Notas%20Importantes) y [Notas sobre las variables](#notas-sobre-las-variables).

Indexator viene con **4 funciones** para indexar las notas de Obsidian. Para los ejemplos de este apartado y los siguientes, usaremos el esquema visto en el apartado [Cómo usar](#cómo-usar).
- `Indexator`. Crea índices ordenados **con números** a partir de encabezados ***sin numeros*** y ***sin Índice de contenidos*** creado (como el del ejemplo). Usado la primera vez que se quiere indexar.

_Ejemplo de índice creado con la función `Indexator`_
```
# Índice de contenidos
- [1. Definición de rendimiento](#1.%20Definición%20de%20rendimiento)
- [2. Métricas populares](#2.%20Métricas%20populares)
	- [2.1 Tiempo de ejecución](#2.1%20Tiempo%20de%20ejecución)
	- [2.2 Otras métricas de rendimiento](#2.2%20Otras%20métricas%20de%20rendimiento)
- [3. Ley de Amdahl](#3.%20Ley%20de%20Amdahl)
- [4. Cómo comparar resultados](#4.%20Cómo%20comparar%20resultados)
- [5. Programas de Prueba (Benchmarks)](#5.%20Programas%20de%20Prueba%20(Benchmarks))
---
```
_Cómo se vería en Obsidian:_

<div align="center">
    <img src="img/Ejemplo salida indexator.png" alt="Ejemplo salida indexator">
</div>

___Nota: Mi Obsidian tiene temas y snippets, pero la estructura del índice será la misma.___

- `Quasi-Indexator`. Crea índices ordenados a partir de encabezados ***con o sin numeros***. Lo único que hace es crear un **Índice de contenidos** a partir de los encabezados que tengas, sin añadir nada. De esta manera, puede usarse si habías puesto numeros de antemano.

- `Re-Indexator`. **Actualiza el índice**. Funciona como una _versión mejorada_ de `Indexator`. El punto de esta función es **crear un índice de nuevo** cuando ya se ha creado uno con el programa (o no), bien porque has añadido o eliminado contenido a tu nota (al principio o final).
	- Está función es muy flexible, y podría reemplazar a todas las funciones del programa. **Si dudas sobre qué función usar**, usa `Re-Indexator`.

- `De-Indexator`. Borra el **Índice de Contenidos** y los índices de los títulos.
## Variables

Durante la ejecución, puedes cambiar los valores de **4 variables** para modificar la salida del programa. Todas estas variables pueden usarse en conjunto, lo que hace que el indexado sea muy flexible.  
- `SUBDIVISION`. Su valor predeterminado es `False`. Cuando vale `True`, añade `INDEX` al frente de los números del índice.

	- De esta manera, la transformación que hace el programa sería la siguiente:
	```
	## -> INDEX.1
	### -> INDEX.1.2
	#### -> INDEX.1.2.3
	#### -> INDEX.1.2.3.4
	##### -> INDEX.1.2.3.4.5
	###### -> INDEX.1.2.3.4.5.6
	```

	- Tomando el ejemplo, si hubiéramos utilizado Indexator con `SUBDIVISION = True`, la salida hubiera sido:
	```
	# Índice de contenidos
	- [1.1 Definición de rendimiento](#1.1%20Definición%20de%20rendimiento)
	- [1.2 Métricas populares](#2%20Métricas%20populares)
		- [1.2.1 Tiempo de ejecución](#1.2.1%20Tiempo%20de%20ejecución)
		- [1.2.2 Otras métricas de rendimiento](#1.2.2%20Otras%20métricas%20de%20rendimiento)
	- [1.3 Ley de Amdahl](#1.3%20Ley%20de%20Amdahl)
	- [1.4 Cómo comparar resultados](#1.4%20Cómo%20comparar%20resultados)
	- [1.5 Programas de Prueba (Benchmarks)](#1.5%20Programas%20de%20Prueba%20(Benchmarks))
	---
	```

- `INDEX`. Su valor predeterminado es `1`. Solo se usa cuando `SUBDIVISION = True`.


- `IGNORE_HEADERS`. Indica qué tamaños de encabezado se ignoran (no se ponen en el índice). Ignora los encabezados mayores o iguales a `hN`, siendo `N` el valor de `IGNORE_HEADERS`. 
	- Su valor por defecto es 0, lo que signfica que **no se ignorará ningun encabezado**.
	- **Sus valores válidos van desde 2-6** (Indexator no trata con encabezados h1). Supongamos el mismo ejemplo de antes, si `IGNORE_HEADERS = 3` entonces el **Índice de contenidos** usando `Indexator` quedaría así:
```
# Índice de contenidos
- [1. Definición de rendimiento](#1.%20Definición%20de%20rendimiento)
- [2. Métricas populares](#2.%20Métricas%20populares)
- [3. Ley de Amdahl](#3.%20Ley%20de%20Amdahl)
- [4. Cómo comparar resultados](#4.%20Cómo%20comparar%20resultados)
- [5. Programas de Prueba (Benchmarks)](#5.%20Programas%20de%20Prueba%20(Benchmarks))
---
```

- `NO_INDEX_HEADERS`. Indica qué tamaños de encabezado **no se indexan**. No indexa los encabezados mayores o iguales a `hN`, siendo `N` el valor de `NO_INDEX_HEADERS`.

	- Su valor por defecto es 0, lo que equivale a indexar todos los encabezados.
	- **Sus valores válidos van desde 2-6**. Supongamos el ejemplo anterior, imaginemos que queremos dejar los encabezados `h3` en el índice, pero no queremos indexarlos. Entonces usariamos `Indexator` con `NO_INDEX_HEADERS = 3`, lo que nos daría:
```
# Índice de contenidos
- [1. Definición de rendimiento](#1.%20Definición%20de%20rendimiento)
- [2. Métricas populares](#2.%20Métricas%20populares)
	- [Tiempo de ejecución](#Tiempo%20de%20ejecución)
	- [Otras métricas de rendimiento](#Otras%20métricas%20de%20rendimiento)
- [3. Ley de Amdahl](#3.%20Ley%20de%20Amdahl)
- [4. Cómo comparar resultados](#4.%20Cómo%20comparar%20resultados)
- [5. Programas de Prueba (Benchmarks)](#5.%20Programas%20de%20Prueba%20(Benchmarks))
---
```

### Notas sobre las variables
- La variable `SUBDIVISION` es tomada en cuenta en las funciones `Indexator` y `Re-Indexator`, pero estas no detectan si los encabezados han sido creados usando esta opción. Tómemos el siguiente ejemplo:
	```
	## 2.1 Definición de rendimiento
	## 2.2 Métricas populares
	### 1.2.1 Tiempo de ejecución
	### 2.2.2 Otras métricas de rendimiento
	#### MIPS
	#### MFLOPS
	## 2.3 Ley de Amdahl
	## 2.4 Cómo comparar resultados
	### Tiempo Total de Ejecución
	### Tiempo Total de Ejecución Ponderado
	### Tiempo Normalizado
	## 2.5 Programas de Prueba (Benchmarks)
	## Ejercicios Resueltos
	```
	- En este caso, yo quiero indexar los nuevos apartados. Si quisiera conservar el `2.` delante de cada título al usar `Re-Indexator`, debo especificar de nuevo que `SUBDIVISION = True` e `INDEX = 2`. El índice resultante se vería así:

		```
		## 2.1 Definición de rendimiento
		## 2.2 Métricas populares
		### 2.2.1 Tiempo de ejecución
		### 2.2.2 Otras métricas de rendimiento
		#### 2.2.2.1 MIPS
		#### 2.2.2.2 MFLOPS
		## 2.3 Ley de Amdahl
		## 2.4 Cómo comparar resultados
		### 2.4.1 Tiempo Total de Ejecución
		### 2.4.2 Tiempo Total de Ejecución Ponderado
		### 2.4.3 Tiempo Normalizado
		## 2.5 Programas de Prueba (Benchmarks)
		## 2.6 Ejercicios Resueltos
		```
	- Nótese que podríamos haber cambiado el `2.` por cualquier otro número modificando el valor de `INDEX` o, en su defecto, haberlo quitado, especificando que `SUBDIVISION = False`.

‎ 
- Si quisiéramos indexar sin poner el **Índice de contenidos**, usaríamos cualquiera de las funciones con `IGNORE_HEADERS = 2`.
- Si no quisiéramos indexar los encabezados, pero sí dejar el **Índice de contenidos**, usaríamos `NO_INDEX_HEADERS = 2`.

- Usar las dos opciones anteriores con `Re-Indexator` equivale a usar `De-Indexator`.

- Usar `Re-Indexator` con `NO_INDEX_HEADERS = 2` equivale a usar `Quasi-Indexator`.

## Presets
Para evitar tener que memorizar los valores de las variables para un tipo de indexado que hagas recurrentemente, el programa te permite crear **presets**: configuraciones de variables que puedes usar para indexar. Estas configuraciones se guardan en el archivo `presets.json`.

Para crear un preset, usa la opción 12 del menú. Se te pedirá un nombre y los valores de las variables. Esto último requiere ser introducido siguiendo un patrón ordenado:
```
             subdivision     index     ignore_headers     no_index_headers
```

A continuación se muestran algunos ejemplos de entradas que acepta el programa:
```
True 1 0 0       # Indexado normal con subíndice 1
False 2 0 0      # Indexado normal (subdivision es False)
false 2 3 0      # Indexado sin poner encabezados h3 y superior en el índice
FaLsE 0 3 3      # Ídem pero además sin indexar los encabezados h3 y superior
0 0 3 3          # Ídem al anterior
```
___Notas Importantes:___ 
- `SUBDIVISION` puede tomar valores 1 o 0 en lugar de `True` o `False`, respectivamente. El programa ignora mayúsculas y minúsculas cuando se comprueba su valor.

- El valor de `INDEX` debe ser válido (mayor que 0) aunque `SUBDIVISION` sea `False`.

- Puede haber espacios de más antes/después/entre las variables.

- Cuando se **crea**/**elimina** un preset, el programa solo mostrará mensajes si se produce un error.

Cabe resaltar que estas configuraciones pueden usarse tanto como si se indexa por primera vez como si se quiere volver a indexar, ya que se usa la función `Re-Indexator`.

## Notas Importantes
- El programa **no detecta encabezados** `h1` (una sola almohadilla). Está hecho a propósito, los encabezados `h1` se ven demasiado grandes para las notas de Obsidian y personalmente no me gusta como quedan.

- El programa no detecta encabezados escritos en bloques de código (todo lo que esté entre backsticks, ```), como pueden ser los ejemplos de este readme.

- Cuando se usa la función `Re-Indexator` o `De-Indexator`, es muy importante que el formato sea preciso:
	- <strong>Si pasas el bruto <u>con índice</u></strong>, es muy importante que esté escrito entre "---", de la siguiente manera:
	```
	---
	## 1. Titulo de ejemplo 1
	## 2. Titulo de ejemplo 2
	### 2.1 Titulo de ejemplo 2.1
	---
	```
	- <strong>Si pasas el bruto <u>sin índice</u></strong>, no tienes que preocuparte por nada, pero téngase en cuenta que el programa detecta que el bruto no tiene índice **si no encuentra el encabezado** `# Índice de contenidos` al principio del documento.

	- En ambos casos, el índice se borrará y se creará uno nuevo. Es de gran importancia que se cumpla el formato especificado, de lo contrario el programa podría no borrar el índice o no indexar correctamente.
