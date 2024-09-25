# Indexator

Indexator es un programa simple de Python que crea **índices Markdown**. Está pensado para ser usado en ***Obsidian***.

Es un programa hecho a mis gustos y a mi manera de organizar los apartados, por lo que la estructura puede no ser como te gustaría (en cuyo caso, siéntete libre de modificar el programa a tu gusto).

## Índice de contenidos
- [Requisitos](#Requisitos)
- [¿Cómo usar?](#¿Cómo%20usar?)
- [Funciones](#Funciones)
- [Configuración](#Configuración)
- [Notas Importantes](#Notas%20Importantes)

___Nota: este índice no ha sido creado con Indexator___

## Requisitos
Python 3.8 o superior: Puedes ver tu versión de Python con `python --version` o `python3 --version`.

## ¿Cómo usar?
Imaginemos que tenemos una nota de obsidian con el siguiente esquema (supongamos que entre los encabezados hay texto):

```
## Definición de rendimiento
## Métricas populares
### Tiempo de ejecución
### Otras métricas de rendimiento
## Ley de Amdahl
## Cómo comparar resultados
## Programas de Prueba (Benchmarks)

```
Un índice se creará a partir de los encabezados markdown (las almohadillas #). Dependiendo del numero de almohadillas, el programa detecta y crea un subíndice. La transformación que hace el programa es la siguiente:
```
## -> 1.
### -> 1.1
#### -> 1.1.2
#### -> 1.1.2.3
##### -> 1.1.2.3.4
###### -> 1.1.2.3.4.5
```

**Para crear un índice de nuestra nota**, copiamos directamente todo el texto anterior de la nota al archivo `bruto.md`. No es necesario copiar solamente los encabezados, podemos copiar el texto completo (incluidas etiquetas) en el caso de que hubiera. El programa simplemente lo ignorará.

Una vez hecho esto, abrimos una terminal en la carpeta del proyecto y ejecutamos el programa:
```python
python main.py
```
Dentro del programa, **seleccionamos la función que queramos usar** (ver [_Funciones_](#Funciones)). El archivo `bruto_indexado.md` contendrá **el bruto con los encabezados modificados** (con los números añadidos) y **el índice** pegado al principio de la nota.

## Funciones
***Antes de usar cualquiera de las siguientes funciones***, ver las [Notas Importantes](#Notas%20Importantes).

Indexator viene con 3 funciones para crear los índices:
- **Indexator**. Crea índices ordenados **con números** a partir de encabezados _sin numeros_ (como el del ejemplo).

- **Quasi-Indexator**. Crea índices ordenados **sin números** a partir de encabezados _con o sin numeros_. De esta manera, puede usarse si habías puesto numeros de antemano, por ejemplo:

```
Ejemplo de contenido de bruto.md para usar función Quasi-Indexator

## 1. Definición de rendimiento
## 2. Métricas populares
### 2.1 Tiempo de ejecución
### 2.2 Otras métricas de rendimiento
## 3. Ley de Amdahl
## 4. Cómo comparar resultados
## 5. Programas de Prueba (Benchmarks)
```

- **Re-Indexator**. **Actualiza el índice**. Funciona como una _versión mejorada_ de **Indexator**. El punto de esta función es **crear un índice de nuevo** cuando ya se ha creado uno con **Indexator** (o no), bien porque has añadido o eliminado contenido a tu nota (al principio o final).


_Ejemplo de índice creado con la función **Indexator**_
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

## Configuración

Durante la ejecución, puedes cambiar los valores de **2 variables** para modificar la salida del programa:
- **SUBDIVISION**. Su valor predeterminado es `False`. Cuando vale `True`, añade **INDEX** al frente de los números del índice.

De esta manera, la transformación que hace el programa sería la siguiente:
```
## -> INDEX.1
### -> INDEX.1.2
#### -> INDEX.1.2.3
#### -> INDEX.1.2.3.4
##### -> INDEX.1.2.3.4.5
###### -> INDEX.1.2.3.4.5.6
```

_Tomando el ejemplo anterior, si hubiéramos utilizado Indexator con **SUBDIVISION** = `True`, la salida hubiera sido:_
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

- **INDEX**. Su valor predeterminado es `1`. Sólo se usa cuando **SUBDIVISION** = `True`.

## Notas Importantes
- Cualquier línea que empiece por dos almohadillas y un espacio (## ) **será tomada como encabezado, aunque no lo sea**. Tener en cuenta si tu archivo contiene estos carácteres entre backsticks ```. Por esta razón no se ha usado **Indexator** para crear el Índice de este readme.

- El programa **no detecta encabezados** `h1` (una sola almohadilla). Está hecho a propósito, los encabezados `h1` se ven demasiado grandes para las notas de Obsidian.

- Cuando se usa la función **Re-Indexator**, es muy importante que el formato sea preciso:
	- **Si pasas el bruto con índice**, es muy importante que esté escrito entre "---", de la siguiente manera:
	```
	---
	## 1. Titulo de ejemplo 1
	## 2. Titulo de ejemplo 2
	### 2.1 Titulo de ejemplo 2.1
	---
	```
	- **Si pasas el bruto sin índice**, no tienes que preocuparte por nada. Nota que el programa detecta que no tiene índice **si no encuentra el encabezado** `# Índice de contenidos`.
En ambos casos, el índice se desechará y se creará uno nuevo, pero es importante que el bruto permanezca intacto (por ello la meticulosidad con el formato).

- La variable **SUBDIVISION** es usada en las funciones **Indexator** y **Re_Indexator**. Podemos jugar con **Re_Indexator** y **SUBDIVISION** para hacer cambios en el formato de los índices. Por ejemplo, tenemos el siguiente contenido:
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
En este caso, si quisiera conservar el `2.` delante de cada título, deberemos especificar que **SUBDIVISION** = `True` e **INDEX** = 2. El índice resultante se vería así:

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

- Sin embargo, podríamos haber cambiado el `2.` por cualquier otro número modificando el valor de **INDEX** o, en su defecto, haberlo quitado, especificando que **SUBDIVISION** = `False`.
