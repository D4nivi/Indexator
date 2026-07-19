#Windows #Tutoriales
--
---
## 3.1 Activar Windows
Una vez hayas instalado Windows y aparezcas en el escritorio, lo primero que recomiendo es <span style="color:rgb(255, 0, 90)"><b>activar Windows</b></span>, aunque podrías ponerte directamente a actualizar primero, el orden en este caso no es critico.

Para activar Windows, usaría [MAS](https://massgrave.dev) (_Microsoft Activation Scripts_). Simplemente abre una Powershell <span style="color:rgb(255, 0, 90)"><b>como administrador</b></span> y ejecuta este comando.
```powershell
irm https://get.activated.win | iex
```

Se abrirá una terminal como esta:

![[3.1 Terminal con opciones de MAS.png|500]]
<p style="text-align: center"><i><b>Terminal con opciones de MAS</b></i><br>­</p>

Pulsa la <span style="color:rgb(142, 255, 20)"><b>tecla 1</b></span> y espera a que el programa termine de trabajar.

![[3.1 Activación de Windows con MAS terminada.png]]
<p style="text-align: center"><i><b>Activación de Windows con MAS terminada</b></i></p>

## 3.2 Actualizar sistema
Nada más activar Windows, lo primero que deberías hacer es <span style="color:rgb(45, 235, 178)"><b>ir a Windows Update y buscar actualizaciones para el sistema</b></span>. Este proceso tardará bastante, pero <span style="color:rgb(255, 192, 0)"><b>es lo primero que deberías hacer <u>antes de seguir con los siguientes pasos</u></b></span>.

![[3.2 Ventana de Windows Update.png|500]]
<p style="text-align: center"><i><b>Ventana de Windows Update</b></i><br>­</p>

Cuando actualices todo y reinicies, vuelve a la ventana de Windows Update y <span style="color:rgb(217, 128, 250)"><b>comprueba de nuevo que no haya más actualizaciones pendientes</b></span> por instalar.
## 3.3 Instalar drivers de dispositivo
Si tu placa base es moderna, seguramente nada más instalar el ordenador te haya salido un popup para <span style="color:rgb(45, 235, 178)"><b>instalar software de drivers del fabricante</b></span>, con el que poder instalar todos los drivers para tu PC. Si no es el caso, <span style="color:rgb(8, 161, 247)"><b>busca cual es el programa para actualizar drivers de tu placa base</b></span> e instálalo. Si no hay otra opción, <span style="color:rgb(255, 192, 0)"><b>descarga e instala los drivers a mano</b></span>.

Por ejemplo, en mi portátil tengo instalado <span style="color:rgb(255, 0, 0)"><b>Lenovo Vantage</b></span>.

![[3.3 Pestaña de actualización de drivers de Lenovo Vantage.png]]
<p style="text-align: center"><i><b>Pestaña de actualización de drivers de Lenovo Vantage</b></i><br>­</p>

>[!warning] Importante
>Mientras que la aplicación esté instalando los drivers, <span style="color:rgb(142, 255, 20)"><b>no intentes instalar otros drivers</b></span> (p.e. drivers de NVIDIA, drivers de tarjetas de audio o wifi, etc), por seguridad. 
## 3.4 Instalar drivers de NVIDIA
Para instalar los <span style="color:rgb(1, 206, 22)"><b>drivers de NVIDIA</b></span>, debemos instalar la [app de NVIDIA](https://www.nvidia.com/es-la/software/nvidia-app/).

Una vez instalada, te aparecerá la pantalla principal de la app pidiéndote que <span style="color:rgb(45, 235, 178)"><b>selecciones el controlador a instalar</b></span>. Selecciona <span style="color:rgb(255, 0, 90)"><b>Controladores Game Ready</b></span>. Deja activada la superposición de NVIDIA si te lo pide, puede molar.

![[Imagen cuando la tenga D:]]

Una vez hecho esto, ve a la pestaña controladores a la izquierda y dale a Descargar.

![[Imagen cuando la tenga D:]]

Debería aparecer una ventana como la siguiente; dale a <span style="color:rgb(8, 161, 247)"><b>instalación personalizada</b></span> y marcas la casilla <span style="color:rgb(217, 128, 250)"><b>"Instalación correcta"</b></span>. Esta opción eliminaría el driver de NVIDIA que traía Windows por defecto, instalaría el driver nuevo y lo cargaría.

![[Imagen cuando la tenga D:]]
## 3.5 Limpieza de bloatware: Win11Debloat
En Windows hay un montón de <span style="color:rgb(255, 192, 0)"><b>aplicaciones de mierda que no vas a usar nunca</b></span>. Por suerte, podemos usar la herramienta [Win11Debloat](https://github.com/Raphire/Win11Debloat) para eliminarlas.

Para usarla, abre una Powershell y pon el siguiente comando:
```powershell
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))
```

Se abrirá una ventana como esta:

![[3.5 Pantalla principal de Win11Debloat.png|500]]
<p style="text-align: center"><i><b>Pantalla principal de Win11Debloat</b></i><br>­</p>

En esta pantalla, seleccionamos <span style="color:rgb(8, 161, 247)"><b><i>Custom Setup</i></b></span>. En la siguiente ventana, podrás ver las <span style="color:rgb(1, 206, 22)"><b>aplicaciones que se desinstalarán de Windows</b></span> (solo las verdes por defecto). Recomiendo echar un vistazo a las aplicaciones que se desinstalarán por si acaso.

![[3.5 Pantalla de desinstalación de aplicaciones de Win11Debloat.png|600]]
<p style="text-align: center"><i><b>Pantalla de desinstalación de aplicaciones de Win11Debloat</b></i><br>­</p>

En la siguiente pantalla, se pueden seleccionar ciertos ajustes a aplicar para <span style="color:rgb(45, 235, 178)"><b>mejorar el rendimiento de Windows</b></span>, entre otras cosas. Es parecida a la [pestaña de Tweaks de winutil](); de hecho, tienen opciones comunes. Recomiendo el <span style="color:rgb(255, 192, 0)"><b>Quick Select</b></span>.

![[3.5 Pantalla de tweaks de Win11Debloat.png]]
<p style="text-align: center"><i><b>Pantalla de tweaks de Win11Debloat</b></i><br>­</p>

En la siguiente pantalla asegúrate de que <span style="color:rgb(172, 79, 243)"><b>creas un punto de restauración</b></span> y dale a aplicar cambios.

![[3.5 Pantalla final de Win11Debloat.png|500]]
<p style="text-align: center"><i><b>Pantalla final de Win11Debloat</b></i><br>­</p>

Cuando terminé, habrá eliminado quizá <span style="color:rgb(142, 255, 20)"><b>poco más de 1 GB</b></span>, pero tendrás un montón de mierda menos en el menú de inicio y menos subprocesos corriendo.

![[3.5 Pantalla de finalización de Win11Debloat.png|400]]
<p style="text-align: center"><i><b>Pantalla de finalización de Win11Debloat</b></i></p>

## 3.6 Ajustes con winutil
### 3.6.1 Tweaks
Con [winutil](https://github.com/ChrisTitusTech/winutil), puedes seleccionar varios ajustes para aplicar a tu instalación de Windows que pueden mejorar el rendimiento y la experiencia. Muchas de estas cosas ya habrán sido hechas si has instalado Windows usando los pasos del [[Daniel/Instalación Windows/1. Preparación#1.1.2 Usando winutil|apartado 1.1.2]] o has usado [Win11Debloat]().

Para <span style="color:rgb(255, 0, 90)"><b>lanzar winutil</b></span>, abre una Powershell <span style="color:rgb(255, 0, 90)"><b>como administrador</b></span> y ejecuta el siguiente comando:
```powershell
irm "https://christitus.com/win" | iex
```

El creador recomienda usar el botón de <span style="color:rgb(1, 206, 22)"><b>tweaks estándar</b></span>, y <span style="color:rgb(255, 192, 0)"><b>no hacer ni caso a los <u>tweaks avanzados</u></b></span>. Yo puedo recomendar los siguientes tweaks esenciales y avanzados. Tras marcarlos, dale al botón <span style="color:rgb(142, 255, 20)"><b><i>Run Tweaks</i></b></span> para aplicarlos.

![[3.6.1 Tweaks recomendados de winutil.png|550]]
<p style="text-align: center"><i><b>Tweaks esenciales recomendados de winutil</b></i><br>­</p>

![[3.6.1 Tweaks avanzados recomendados de winutil.png]]
<p style="text-align: center"><i><b>Tweaks avanzados recomendados de winutil. Nótese que he puesto el DNS de Cloudflare</b></i><br>­</p>

Si quieres <span style="color:rgb(217, 128, 250)"><b>revertir los tweaks</b></span>, puedes marcar de nuevo los tweaks a deshacer y darle al botón de <span style="color:rgb(142, 255, 20)"><b><i>Undo Selected Tweaks</i></b></span>. También puedes <span style="color:rgb(10, 112, 217)"><b>restaurar a un punto anterior</b></span> de aplicar los tweaks si marcaste el tweak de crear punto de restauración.

>[!note] Nota
>El tweak de <span style="color:rgb(8, 161, 247)"><b><i>Disk Cleanup</i></b></span> podría tardar mucho tiempo, no te preocupes.

A la derecha de los tweaks hay otra serie de <span style="color:rgb(106, 71, 249)"><b>preferencias de Windows</b></span> que puedes cambiar. No afectan directamente al rendimiento, sino a la experiencia de usuario. Míralas y <span style="color:rgb(255, 0, 90)"><b>marca las que te interesen</b></span>.
### 3.6.2 Instalación rápida de software
Muchas de las aplicaciones que más uso a diario pueden ser <span style="color:rgb(255, 0, 90)"><b>instaladas automáticamente con winutil</b></span>, en lugar de ir manualmente a la página de descarga e instalar. Simplemente ve seleccionando en la pantalla y dale a instalar.

![[3.6.2 Instalación de software con winutil.png]]

Cuando haya terminado, la barra de abajo pondrá <span style="color:rgb(142, 255, 20)"><b><i>App install finished</i></b></span>. He probado y <span style="color:rgb(8, 161, 247)"><b>las siguiente aplicaciones están disponibles y se instalan correctamente</b></span>: Discord, Steam, Epic Games, Audacity, VLC, HWMonitor, HWInfo, Rufus, VS Code, Proton Pass, WinRAR, Crystal Disk Mark, Obsidian, VirtualBox y Python (última versión)[^2].
- WinRAR tendrás que crackearlo igualmente.

Si alguna instalación no te convence, siempre puedes <span style="color:rgb(217, 128, 250)"><b>desinstalar los programas con un botón</b></span>.

>[!note] Nota
>Puede ser que algunas aplicaciones <span style="color:rgb(255, 0, 90)"><b>se instalen como comandos</b></span>, y no tengan un ejecutable accesible desde el menú de Inicio (al final, todo se instala con <span style="color:rgb(45, 235, 178)"><b>WinGet</b></span>).
>
>Un ejemplo de esto es <span style="color:rgb(255, 192, 0)"><b>Rufus</b></span>: cuando lo instalas, en realidad estás instalando un programa usable sólo desde la terminal (Rufus por defecto es solo un ejecutable portable, así que tiene sentido).
## 3.7 Instalación completada
Si has llegado hasta aquí, la instalación de Windows ha terminado, y tienes Windows 11 con mucha menos mierda y mejor rendimiento. A continuación, dejo <span style="color:rgb(255, 0, 90)"><b>algunas otras cosas que puedes hacer después de hacer todo lo anterior</b></span>:
- Instalar programas que falten (ver nota de [[Daniel/Instalación Windows/Software|Software]] y disco duro).
- Cambiar <span style="color:rgb(8, 161, 247)"><b>cursores</b></span>[^1].
- Modificar <span style="color:rgb(45, 235, 178)"><b>aplicaciones de inicio</b></span>.
- <span style="color:rgb(255, 192, 0)"><b>Quitar ciertas aplicaciones de segundo plano</b></span> (en Windows 11, Aplicaciones $\rightarrow$ Aplicaciones instaladas $\rightarrow$ click en los tres puntos de una app $\rightarrow$ Opciones Avanzadas).
### 3.7.1 Cambiar mapeo de tecla de copilot
Si compras un portátil moderno, probablemente tenga la <span style="color:rgb(255, 0, 90)"><b>tecla de Copilot</b></span> en el teclado. Esta tecla es una mierda y no lo vas a usar, porque has desinstalado Copilot.

![[3.7.1 Tecla de copilot.png|600]]
<p style="text-align: center"><i><b>Tecla de copilot</b></i><br>­</p>

Ahora, lo que puedes hacer es <span style="color:rgb(45, 235, 178)"><b>hacer que esta tecla funcione como la tecla Ctrl</b></span>, que es la tecla que debería ser. Esto puede hacerse de dos formas:
1. Usando [AutoHotkey](https://www.autohotkey.com) (<span style="color:rgb(1, 206, 22)"><b>recomendado</b></span>). Instala el programa y descarga [éste archivo](https://drive.google.com/file/d/1HoWfY1zWY3LYYb52ftES0elKhF-IScde/view?usp=drive_link) del drive. Presiona `Windows + R` y escribe `shell:startup`. Se abrirá una carpeta; mete allí un <span style="color:rgb(255, 192, 0)"><b>acceso directo al fichero que acabas de descargar</b></span> (guarda el original).

![[3.7.1 Comando de Windows + R y carpeta donde poner el acceso directo al script.png|600]]
<p style="text-align: center"><i><b>Comando de Windows + R y carpeta donde poner el acceso directo al script</b></i><br>­</p>

2. Usando [[Daniel/Instalación Windows/Software#PowerToys|PowerToys]]. En este caso, usaremos la utilidad de <span style="color:rgb(8, 161, 247)"><b>Administrador de teclado</b></span>.

![[3.7.1 Utilidad de PowerToys para reasignación de tecla copilot.png]]
<p style="text-align: center"><i><b>Utilidad de PowerToys para reasignación de tecla copilot</b></i><br>­</p>

Le damos al botón de <span style="color:rgb(45, 235, 178)"><b>reasignar un acceso directo</b></span>. Agregamos una reasignación de acceso como la siguiente: a la izquierda pulsamos la <span style="color:rgb(255, 0, 90)"><b>tecla de copilot</b></span>; a la derecha, seleccionamos la tecla <span style="color:rgb(255, 192, 0)"><b>Ctrl derecho</b></span>.

![[3.7.1 Reasignación de acceso directo para tecla copilot.png]]
<p style="text-align: center"><i><b>Reasignación de acceso directo para tecla copilot</b></i><br>­</p>

>[!info] Dato mata relato
>Como puedes ver en la imagen de arriba, la tecla de Copilot en realidad manda una <span style="color:rgb(106, 71, 249)"><b>combinación de tres teclas</b></span> al ser pulsada: `Win (Left) + Shift (Left) + F23`. Esto también se puede ver en el script de AutoHotkey.

Esto debería funcionar, pero si tienes activado el `FnLock`, la tecla de copilot manda `AppsMenu` en lugar de la combinación anterior. Para que el mapeo funcione en este caso, dale a <span style="color:rgb(8, 161, 247)"><b>Reasignar una tecla</b></span>. En esta ventana, añade la siguiente reasignación de teclas:

![[3.7.1 Reasignación de teclas para tecla copilot.png|600]]
<p style="text-align: center"><i><b>Reasignación de teclas para tecla copilot (para tener en cuenta el FnLock)</b></i><br>­</p>

Si esto te parece un porculo, <span style="color:rgb(255, 192, 0)"><b>es porque lo es</b></span>, usa el otro método que es más fácil.

---
___Fin de la Instalación___

___Ver:___ [[4. Mantenimiento]]
___Ver:___ [[Daniel/Instalación Windows/Software|Software]]

[^1]: Recuerda meter los archivos de cursores en la carpeta `C:\Windows\Cursors`.

[^2]: El único programa que no pudo instalar (de los que probé) fue [Parsec](https://parsec.app/downloads).