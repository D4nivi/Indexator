# Indexator

Indexator es un programa simple de Python que crea índices para Obsidian.

## ¿Cómo usar?
Imaginemos que tenemos una nota de obsidian con el siguiente esquema (los ... representan texto):

```
## Definición de rendimiento
...
...

## Métricas populares
...

### Tiempo de ejecución
...

### Otras métricas de rendimiento
...
...

## Ley de Amdahl
...
...

## Cómo comparar resultados
...


## Programas de Prueba (Benchmarks)
...

```
Un índice se creará a partir de los encabezados markdown (las almohadillas #). Dependiendo del numero de almohadillas, el programa detecta y crea un subindice. La transformación que hace el programa es la siguiente:
```
## -> 1.
### -> 1.1
#### -> 1.1.2
#### -> 1.1.2.3
##### -> 1.1.2.3.4
###### -> 1.1.2.3.4.5
```

Para crear un índice de nuestra nota, copiamos directamente todo el texto anterior de la nota al archivo `bruto.md`. No es necesario copiar solamente los encabezados, podemos copiar el texto completo (incluidas etiquetas) en el caso de que hubiera. El programa simplemente lo ignorará.

Una vez hecho esto, ejecutamos el programa y seleccionamos la función que queramos usar (ver [_Funciones_](#Funciones)). El archivo `indice.md` contendrá el indice, mientras que el archivo `bruto_indexado.md` contendrá el bruto con los encabezados modificados (con los números añadidos).


### Funciones

Indexator viene con 2 funciones para crear los indices:
- **Indexator**. Crea índices ordenados **con números** a partir de encabezados _sin numeros_ (como el del ejemplo).

- **Quasi-Indexator**. Crea índices ordenados **sin números** a partir de encabezados _con o sin numeros_. De esta manera, puede usarse si habías puesto numeros de antemano, por ejemplo:
```
## 1. Definición de rendimiento
## 2. Métricas populares
### 2.1 Tiempo de ejecución
### 2.2 Otras métricas de rendimiento
## 3. Ley de Amdahl
## 4. Cómo comparar resultados
## 5. Programas de Prueba (Benchmarks)
```

_Ejemplo de salida de función **Indexator** en `indice.md`._
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
_Cómo se veria en Obsidian:_
![](https://github.com/D4nivi/Indexator/blob/main/img/Ejemplo%20salida%20indexator.png)

### Configuración

Durante la ejecución, puedes cambiar los valores de 2 variables para modificar la salida del programa:
- **SUBDIVISION**. Su valor predeterminado es `False`. Cuando vale `True`, añade **INDEX** al frente de los números del índice. Útil si creas apuntes por temas.

De esta manera, la transformación que hace el programa sería la siguiente:
```
## -> INDEX.1
### -> INDEX.1.2
#### -> INDEX.1.2.3
#### -> INDEX.1.2.3.4
##### -> INDEX.1.2.3.4.5
###### -> INDEX.1.2.3.4.5.6
```

_Usando el ejemplo anterior, si hubieramos utilizado Indexator con **SUBDIVISION** = `True`, la salida hubiera sido:_
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

- **INDEX**. Su valor predeterminado es `1`. Solo se usa cuando **SUBDIVISION** = `True`.


