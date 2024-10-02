#Linux
--
---
# Índice de contenidos
- [1. ¿Qué es un _alias_?](#1.%20¿Qué%20es%20un%20_alias_?)
- [2. Cómo crear/eliminar un _alias_](#2.%20Cómo%20crear/eliminar%20un%20_alias_)
---
## 1. ¿Qué es un _alias_?
Un <span style="color:rgb(0, 209, 139)"><b>alias</b></span> es una cadena de caracteres que nosotros definiremos y que servirá para ejecutar un comando determinado. Es por así decirlo, una <span style="color:rgb(0, 209, 139)">abreviatura de un comando</span>, ya que <span style="color:rgb(255, 192, 0)">los alias se suelen usar para sustituir comandos largos y/o difíciles de recordar</span>.
- Un ejemplo de alias sería usar la palabra `updatef` para ejecutar `sudo dnf update && sudo dnf upgrade && sudo flatpak update`.
La principales utilidades y ventajas de los alias en Linux son las siguientes:
1. Reducir el texto escrito en la terminal para realizar una tarea.
2. Sustituir una herramienta por otra herramienta sin tener que cambiar la sintaxis (p.e. sustituir ``ls`` por ``lsd``).
3. Ejecutar un comando simple con opciones adicionales. Por ejemplo, podemos hacer que ejecutando el comando `ls` se ejecute `ls -la`.
## 2. Cómo crear/eliminar un _alias_
La sintaxis para crear un alias es la siguiente:
```shell
alias abreviatura="comando_que_ejecuta_la_abreviatura"
```
Linux permite crear <span style="color:rgb(0, 209, 139)">alias permanentes</span> y <span style="color:rgb(172, 79, 243)">alias temporales</span>. Los alias temporales <span style="color:rgb(172, 79, 243)">solo se aplicarán en la sesión actual de la terminal</span>.
- Para crear un <span style="color:rgb(172, 79, 243)">alias temporal</span>, simplemente introducimos en la terminal el comando alias usando la sintaxis vista arriba.
```shell
alias updatef="sudo dnf update && sudo flatpak update"
```
Para <span style="color:rgb(255, 0, 0)"><strong>eliminar</strong></span> un <span style="color:rgb(172, 79, 243)">alias temporal</span>, puedes usar el comando `unalias`:
```shell
unalias updatef    # elimina el alias updatef
unalias -a         # elimina todos los alias temporales
```
- Para crear un <span style="color:rgb(0, 209, 139)">alias permanente</span>, edita el archivo ``~/.bashrc`` o ``~/.zshrc`` (dependiendo de que _shell_ uses), busca el apartado donde estén los alias y añádelos ahí (puedes ponerlos en cualquier sitio, pero mejor ser ordenado).
```txt
alias lsd="ls"     # alias lsd = "ls" no funcionará. No uses espacios.
```
Para eliminar un <span style="color:rgb(0, 209, 139)">alias permanente</span> no puedes usar el comando ``unalias``, tienes que borrarlo manualmente del archivo ``~/.bashrc`` o ``~/.zshrc``.

![[Ejemplos alias.png|center]]
____[Fuente](https://geekland.eu/alias-en-linux-que-son-como-crearlos-y-ejemplos/)___
