#Linux #Fedora #Tutoriales
--
---
## 3.1 Antes de nada
>[!danger] Importante
>Si al reiniciar no vuelves a Fedora, es completamente normal. <span style="color:rgb(0, 209, 139)">Debes volver a la BIOS/menú del apartado</span> [2.1](2.%20Instalación#2.1%20Booteando%20el%20USB) e <span style="color:rgb(1, 206, 225)">iniciar Fedora desde allí</span>. Deberá aparecer en ambos casos una nueva opción para bootear, con el nombre Fedora o similar.

<span style="color:rgb(236, 54, 109)">Cuando hayas reiniciado y completado la instalación</span>, Fedora aún <span style="color:rgb(0, 209, 139)">no estará listo para usar</span>. Hay algunas cosas que debemos hacer antes de tener nuestro sistema completamente utilizable. Lo primero, <span style="color:rgb(243, 119, 210)">actualizar</span>:
```shell
sudo dnf update
```
- Si al usar el comando sudo nos dice que <span style="color:rgb(225, 71, 71)">no estamos en el archivo sudoers</span>, nos convertimos en superusuario con el comando ``su``. Delante del prompt, el dólar <span style="color:rgb(0, 209, 139)">$</span> se habrá cambiado por un <span style="color:rgb(0, 209, 139)">#</span>, lo que significa que somos superusuarios. Ahora, hacemos: 
```shell
nano /etc/sudoers
```
- Dentro del archivo, buscamos <span style="color:rgb(243, 119, 210)">root</span>. Debería aparecer una línea como la siguiente:
```txt title:"Dentro de /etc/sudoers"
## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL
```
- Debajo de esa línea, <span style="color:rgb(240, 170, 71)">copiamos lo mismo pero cambiamos root por nuestro nombre de usuario</span>. Ahora estamos en la lista de superusuarios (podemos usar el comando sudo).
```txt title:"Dentro de /etc/sudoers"
## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL
danivi  ALL=(ALL)       ALL
```
Después de actualizar, reiniciamos el equipo y empezamos con lo importante.
## 3.2 Configurar Dual Boot
<span style="color:rgb(243, 119, 210)">Para lograr que el menú de GRUB se muestre</span>, es necesario ajustar las <span style="color:rgb(253, 253, 150)">opciones de arranque en la BIOS</span>, para que el sistema arranque desde el gestor de arranque de Linux. 

Para ello, simplemente <span style="color:rgb(1, 206, 225)">ponemos el disco que contiene la instalación de Linux como primera prioridad de arranque</span> y guardamos los cambios. El proceso puede variar dependiendo de la marca/modelo de BIOS.

![[3.1 Prioridades de arranque.jpg|center]]

Una vez tengamos el menú de GRUB funcionando, entramos en Fedora para <span style="color:rgb(0, 209, 139)">ajustar la configuración del GRUB</span>. Editamos el archivo de configuración:
```shell
sudo nano /etc/default/grub
```
Aquí nos interesan 2 opciones:
- <span style="color:rgb(172, 79, 243)"><strong>GRUB_DEFAULT</strong></span>: <span style="color:rgb(243, 119, 210)">cambia la opción de SO predeterminada</span>. El <span style="color:rgb(253, 253, 150)">número</span> que pongas (empezando por 0) corresponde a la <span style="color:rgb(253, 253, 150)">posición del SO que se ve en el menú de GRUB</span> (de arriba a abajo). Por ejemplo, en el menú de GRUB de la imagen, <span style="color:rgb(0, 209, 139)">Windows se encuentra en la posición 3</span>, luego para que Windows se ejecute por defecto: `GRUB_DEFAULT=3`.

![[3.1 Menú de GRUB.jpg|center]]
- <span style="color:rgb(172, 79, 243)"><strong>GRUB_TIMEOUT</strong></span>: <span style="color:rgb(243, 119, 210)">tiempo que espera hasta seleccionar el SO</span> (en segundos). 5 segundos es un tiempo muy adecuado, en mi opinión.

![[3.1 Configurar grub menu.png|center]]

Tras modificar el archivo, guárdalo y <span style="color:rgb(255, 192, 0)">ejecuta el siguiente comando para que los cambios surtan efecto</span> (el comando solo es válido en Fedora):
```shell title:"Actualizar configuración del GRUB"
sudo grub2-mkconfig -o /etc/grub2.cfg
```

>[!tip] ___Curiosidad...___
>_<i><span style="color:rgb(0, 209, 139)"><strong>¿Por qué me aparecen mas de un kernel para mi estación de trabajo en el menú de GRUB?</strong></span></i> La repuesta es muy sencilla: <span style="color:rgb(243, 119, 210)"><strong>Fedora intenta mantener varios núcleos</strong></span> (por defecto 3), <span style="color:rgb(243, 119, 210)"><strong>en caso de que alguno arranque falle</strong></span> y tenga que volver a uno más antiguo y cada cierto tiempo aparecen nuevas versiones del kernel._
>
><i><span style="color:rgb(18, 161, 217)"><strong>Esto se puede cambiar en el siguiente archivo</strong></span></i>:
>`sudo nano /etc/dnf/dnf.conf` _en el siguiente parámetro:_  `installonly_limit=3`
>
><i><span style="color:rgb(253, 253, 150)"><strong>Para ver que versiones de kernel tenemos instaladas</strong></span></i>, usamos el comando `dnf repoquery --installonly`. El comando nos mostrará varios archivos. <i><span style="color:rgb(236, 54, 109)"><strong>Para eliminar un kernel</strong></i></span>, eliminas todos los archivos de una versión con `sudo dnf remove`.
## 3.3 ¿Cómo hacer el dnf más rápido?
Al parecer, el <span style="color:rgb(0, 176, 240)">package manager</span> predeterminado de Fedora (`dnf`) es más lento que los de otras distribuciones. Para hacer que vaya más rápido, podemos hacer unos ajustes. Vamos a editar el siguiente archivo:
```shell
sudo nano /etc/dnf/dnf.conf
```
Dentro del archivo, añadimos las siguientes líneas y guardamos:
```text title:"Dentro del /etc/dnf/dnf.conf"
skip_if_unavailable=True
max_parallel_downloads=20
fastestmirror=True
deltarpm=True
```

>[!note] Nota 
>Para que la línea `deltarpm=True` funcione, es necesario tener instalado <span style="color:rgb(0, 209, 139)"><strong>deltarpm</strong></span>, que debería venir ya instalado en Fedora (si no, usa `sudo dnf install deltarpm`). 
><i><span style="color:rgb(225, 71, 71)"><strong>deltarpm puede no hacer una gran diferencia con conexiones a Internet rápidas</strong></span></i>.
## 3.4 Third-Party Repositories
Un <span style="color:rgb(0, 176, 240)">Repositorio de Terceros</span> (<span style="color:rgb(0, 176, 240)">Third-Party Repository</span>) es cualquier repositorio de software que <span style="color:rgb(0, 209, 139)">el Proyecto Fedora no mantiene oficialmente</span>. 

Hay muchos <span style="color:rgb(253, 253, 150)">programas</span> que no están en los <span style="color:rgb(253, 253, 150)">repositorios de Fedora</span>, por lo que <span style="color:rgb(253, 253, 150)">será necesario tener acceso a repositorios de terceros para instalarlos</span>. 

A continuación muestro como acceder a repositorios que he necesitado para instalar algunas de mis aplicaciones ([[Software#WhatsApp | Whatsapp]], [[Software#Discord | Discord]], [[Software#Spotify y Spicetify | Spotify]]...):
### 3.4.1 RPM Fusion
<span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: [Repositorios RPM](https://rpmfusion.org/Configuration)
```shell
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-40.noarch.rpm
```
```shell
sudo dnf install https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-40.noarch.rpm
```
>[!note] Nota
><span style="color:rgb(255, 192, 0)">Es recomendable instalar los repositorios free primero</span>. Nota que los comandos instalan para Fedora 40. Para hacer el comando más flexible, puedes sustituir 40 por 
`$(rpm -E %fedora)`. A mí personalmente no me funcionó.
### 3.4.2 flathub
<span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: [Flathub](https://flathub.org/setup)
```shell
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

>[!note] Nota
>_Para <span style="color:rgb(255, 192, 0)">actualizar</span> los paquetes instalados con <span style="color:rgb(255, 192, 0)">flatpak</span>, debemos usar el comando_:
> ```shell
> sudo flatpak update
> ```
### 3.4.3 snap
<span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: [snap](https://snapcraft.io/snapd)
```shell
sudo dnf install snapd
```
Los paquetes de <span style="color:rgb(233, 84, 32)"><strong>snap</strong></span> se suelen ejecutar en un entorno altamente confinado, lo que aumenta la <span style="color:rgb(1, 206, 225)"><strong>seguridad</strong></span> y <span style="color:rgb(1, 206, 225)"><strong>estabilidad</strong></span>. Sin embargo, puede haber ciertos paquetes que <span style="color:rgb(236, 54, 109)"><strong>requieran acceso fuera de este confinamiento</strong></span>. Para dárselo, usaríamos el comando:
```shell
sudo ln -s /var/lib/snapd/snap /snap
```
Esto habilita el <span style="color:rgb(45, 235, 178)"><strong>Classic Snap Support</strong></span>, y sólo se debe usar cuando es estrictamente necesario.
## 3.5 Instalación completada
Una vez configurado todo lo anterior, tu Fedora está listo para usar. <span style="color:rgb(255, 192, 0)">Si has instalado Fedora KDE</span>, recuerda hacer algunos ajustes en las <span style="color:rgb(45, 235, 178)"><strong>Preferencias del Sistema</strong></span>:
- Poner un <span style="color:rgb(0, 209, 139)"><strong>Carrusel de fondos</strong></span> (<span style="color:rgb(0, 176, 80)"><strong>Fondos del escritorio</strong></span>).
- Cambiar <span style="color:rgb(253, 253, 150)"><strong>sensibilidad del Mouse</strong></span> a <span style="color:rgb(236, 54, 109)"><strong>-0,80</strong></span> (<span style="color:rgb(0, 176, 80)"><strong>Ratón y panel táctil -> Velocidad del puntero</strong></span>).
- Cambiar la <span style="color:rgb(243, 119, 210)"><strong>foto del perfil</strong></span> de usuario (<span style="color:rgb(0, 176, 80)"><strong>Usuarios</strong></span>).
- Ajustar <span style="color:rgb(255, 192, 0)"><strong>suspensión</strong></span> cada x minutos (<span style="color:rgb(0, 176, 80)"><strong>Bloqueo de pantalla</strong></span>).
- Cambiar <span style="color:rgb(18, 161, 217)"><strong>iconos</strong></span> a los de <span style="color:rgb(10, 112, 217)"><strong>Kora</strong></span> (<span style="color:rgb(0, 176, 80)"><strong>Colores y temas -> Iconos</strong></span>).
- <span style="color:rgb(217, 255, 26)"><strong>Quitar la confirmación</strong></span> al apagar y reiniciar (<span style="color:rgb(0, 176, 80)"><strong>Sesión</strong></span>).
- Poner a [la tía esta](https://www.youtube.com/watch?v=UnIhRpIT7nc) (<span style="color:rgb(0, 176, 80)"><strong>Colores y temas -> Pantalla de bienvenida</strong></span>).
‎
- Quitar opción de <span style="color:rgb(172, 79, 243)"><strong>agrandar el ratón</strong></span> cuando se mueve (<span style="color:rgb(0, 176, 80)"><strong>Accesibilidad -> Sacudir el cursor</strong></span>).  
‎ 
- Quitar/Poner <span style="color:rgb(236, 54, 109)"><strong>Panel flotante</strong></span> (<span style="color:rgb(0, 176, 80)"><strong>Click derecho en el panel -> Configuración de mostrar el panel</strong></span>).
‎ 
- Poner la opción de <span style="color:rgb(1, 206, 225)"><strong>Minimizar ventanas</strong></span> en lugar de Vistazo al escritorio. Es un elemento gráfico, añádelo y cámbialo haciendo <span style="color:rgb(0, 176, 80)"><strong>Click derecho en el botón de Vistazo al escritorio -> Mostrar alternativas</strong></span>.
‎ 
- Arregla el <span style="color:rgb(255, 192, 0)"><strong>problema del cursor grande y feo</strong></span> en algunas aplicaciones. Edita este archivo:
```shell
sudo nano /etc/environment
```
- Y añade lo siguiente (cambia `TuTemaDeCursor` por el tema que quieras usar):
```shell
XCURSOR_THEME=TuTemaDeCursor
XCURSOR_SIZE=32
```
### 3.5.1 Programas que instalar primero (en orden)
```shell
sudo dnf install neofetch
sudo dnf install git     # Necesario para instalar muchos programas

# zsh. Seguir pasos de la nota Software
sudo dnf install zsh

# ohmyzsh. Recuerda instalar los plugins, ver nota Software
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" (ohmyzsh)

# Dependencias para Alacritty y Alacritty
sudo dnf install cmake freetype-devel fontconfig-devel libxcb-devel libxkbcommon-devel g++
git clone https://github.com/alacritty/alacritty.git
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
. "$HOME/.cargo/env"     # El comando de arriba te dirá que hagas esto
cd alacritty; cargo build --release # Seguir pasos de la nota Software
```

---
___Ver:___ [[Software]]
