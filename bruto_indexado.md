#Fedora #Linux #Tutoriales
--
---
## Alacritty
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: Alacritty es un emulador de terminal acelerada por GPU y multiplataforma que permite una amplia configuración.
><span style="color:rgb(0, 209, 139)"><strong>Instalar Alacritty</strong></span>: https://github.com/alacritty/alacritty/blob/master/INSTALL.md
><span style="color:rgb(0, 209, 139)"><strong>Instalar temas</strong></span>: https://github.com/rajasegar/alacritty-themes?tab=readme-ov-file
><span style="color:rgb(0, 209, 139)"><strong>Ver preview de los temas</strong></span>: https://github.com/alacritty/alacritty-theme
><span style="color:rgb(0, 209, 139)"><strong>Guía del archivo de configuración</strong></span>: https://alacritty.org/config-alacritty.html
>![Image link|center|300](https://raw.githubusercontent.com/alacritty/alacritty/master/extra/logo/compat/alacritty-term%2Bscanlines.png)
### Instalación
1. Instalar [rustup.rs](https://rustup.rs/) 
- Si no te lo dice, pon este comando tras instalar:
```shell
. "$HOME/.cargo/env"
```
2. Instalar dependencias:
```shell
sudo dnf install cmake freetype-devel fontconfig-devel libxcb-devel libxkbcommon-devel g++
```
3. Clonamos el repositorio y nos metemos en la carpeta.
```shell
git clone https://github.com/alacritty/alacritty.git
cd alacritty
```
4. Construimos el programa con cargo (package manager de Rust)
```shell
cargo build --release
```
5. Crea la carpeta `alacritty` en `~/.config` y mete el [archivo de configuración](https://drive.google.com/file/d/1oQEjGmPypO1EKlrrWglcodcO2--27FYw/view?usp=drive_link).
```shell
cd ~/.config
mkdir alacritty
```
### Post-Instalación
1. <span style="color:rgb(255, 192, 0)">Para comprobar que el programa funciona correctamente</span>, el siguiente comando no debe dar ningún error.
```shell
infocmp alacritty
```
2. <span style="color:rgb(255, 192, 0)">Para poder usar Alacritty donde sea y que aparezca al buscarlo</span>, hacemos
```shell
sudo cp target/release/alacritty /usr/local/bin # or anywhere else in $PATH
sudo cp extra/logo/alacritty-term.svg /usr/share/pixmaps/Alacritty.svg
sudo desktop-file-install extra/linux/Alacritty.desktop
sudo update-desktop-database
```
- Si hacemos esto, podemos eliminar el repositorio de alacritty de `$HOME`.
3. Pon un <span style="color:rgb(0, 176, 240)">atajo de teclado</span> para Alacritty, por ejemplo, <span style="color:rgb(0, 176, 240)">Ctrl+Alt+T</span>. En KDE busca <span style="color:rgb(0, 176, 80)">Preferencias del sistema -> Atajos de Teclado -> Añadir</span>, busca Alacritty y añádelo.
4. Cuando quieras abrir una terminal con <span style="color:rgb(0, 176, 80)">Click derecho -> Abrir terminal</span>, <span style="color:rgb(225, 71, 71)">no se abrirá Alacritty por defecto</span>, sino <span style="color:rgb(225, 71, 71)">Konsole</span> (en KDE). 

![[Abrir terminal.png|center]]
- Para hacer que se abra una terminal de Alacritty, editamos `~/.config/kdeglobals` y añadimos esta linea en el apartado `[General]`
```text
TerminalApplication=alacritty
```
![[kdeglobals nueva linea.png|center]]
### Temas
Para instalar los <span style="color:rgb(236, 54, 109)"><strong>temas</strong></span> necesitamos tener `npm`, el package manager de <span style="color:rgb(0, 209, 139)"><strong>node.js</strong></span>. Para ello, instalamos <span style="color:rgb(0, 209, 139)"><strong>node.js</strong></span>, que lo lleva incluido consigo:
```shell
sudo dnf install nodejs
```
Ahora instalamos los temas.
```shell
npm i -g alacritty-themes
```
Para <span style="color:rgb(1, 206, 225)"><strong>cambiar el tema</strong></span>, ponemos `alacritty-themes` seguido del <span style="color:rgb(255, 192, 0)"><strong>nombre del tema a usar</strong></span>:
```shell
alacritty-themes Challenger-Deep
```

---
## Discord
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Requisitos</strong></span>: [`rpm`](https://rpmfusion.org/Configuration) ó [`flatpak`](https://flatpak.org/setup/)
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://itsfoss.com/install-discord-fedora/
>
>![Image link|center|400](https://logos-world.net/wp-content/uploads/2020/12/Discord-Emblem.png)
### Instalación
- Puedes instalarlo, si tienes los repositorios non-free de rpm, con `dnf`:
```shell
sudo dnf install discord
```
- Si tenemos flatpak:
```sh
flatpak install discord
```

---
## Eclipse
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Requisitos</strong></span>: [`flatpak`](https://flatpak.org/setup/)
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://developer.fedoraproject.org/tools/eclipse/about.html
><span style="color:rgb(0, 209, 139)"><strong><strong>Página de temas</strong></strong></span>: https://eclipse-color-themes.web.app/
>
>![Image link|center|270](https://cdn.worldvectorlogo.com/logos/eclipse-11.svg)
### Instalación
```sh
flatpak install org.eclipse.Java
```
#### ¿Cómo poner modo oscuro?
Dentro de <span style="color:rgb(255, 192, 0)"><strong>Eclipse</strong></span>, ve a la barra de arriba y busca <span style="color:rgb(0, 209, 139)"><strong><strong>Window -> Preferences -> General -> Appearance</strong></strong></span>. Allí puedes cambiar el tema a modo oscuro.

![[Eclipse modo oscuro.png|center|400]]
### Instalar temas
Descarga mi tema de eclipse desde el [drive](https://drive.google.com/file/d/1LtLfXozuDmAMpiC8wWsQ578vhe8ezLo1/view?usp=drive_link).
1. En <span style="color:rgb(255, 192, 0)"><strong>Eclipse</strong></span>, ve a <span style="color:rgb(0, 209, 139)"><strong><strong>Help -> Eclipse Marketplace</strong></strong></span>. Allí, pon `theme` en la barra de búsqueda, busca <span style="color:rgb(236, 54, 109)"><strong>Darkest Dark Theme with DevStyler</strong></span> e instálalo.

![[Eclipse devstyler.png|center]]

- Tras instalar te pedirá aceptar unas <span style="color:rgb(1, 206, 225)"><strong>licencias</strong></span>: acéptalas, dale a <span style="color:rgb(243, 119, 210)"><strong>Confirm</strong></span> y <span style="color:rgb(0, 209, 139)"><strong>espera que se instale</strong></span>. Puede tardar un poco.
![[Eclipse aceptar licencia.png|center|400]]

2. Cuando termine de instalar, te aparecerá la siguiente pantalla. Marca la palomita y dale a <span style="color:rgb(243, 119, 210)"><strong>Trust Selected</strong></span>. Luego te pedirá <span style="color:rgb(172, 79, 243)"><strong>reiniciar Eclipse</strong></span> (hazlo).

![[Eclipse DevStyle trust selected.png|center|600]]
- <span style="color:rgb(0, 209, 139)"><strong>Si todo ha salido bien</strong></span>, tras el reinicio, te aparecerá una ventana como esta.

![[Eclipse extension de los cojones instalada.png|center|500]]
- Si usas <span style="color:rgb(217, 255, 26)"><strong>Wayland</strong></span>, seguramente te pida que exportes una <span style="color:rgb(236, 54, 109)"><strong>variable de entorno</strong></span> en la terminal llamada `WEBKIT_DISABLE_COMPOSITING_MODE=1`. Hazlo en el `.zshrc`.
```txt title:"Dentro de ~/.zshrc..."
export WEBKIT_DISABLE_COMPOSITING_MODE=1
```
3. Ve a <span style="color:rgb(0, 209, 139)"><strong><strong>Window -> Preferences -> General -> DevStyle</strong></strong></span>. En el apartado extras, dale a <span style="color:rgb(18, 161, 217)"><strong>Import...</strong></span> y selecciona el archivo `.xml` con el tema. Visita [ésta](https://draculatheme.com/eclipse) página para ver un tutorial.

![[Eclipse instalar tema DevStyle.png|center]]

---
## GIMP
>[!Info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: GIMP significa GNU Image Manipulation Program (lol).
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://www.gimp.org/downloads/
>
>![Image link|center|350](https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/The_GIMP_icon_-_gnome.svg/1200px-The_GIMP_icon_-_gnome.svg.png)
### Instalación
>[!note] Nota...
>_...de la página de descarga: **If available, the official package from your Unix-like distribution is the recommended method of installing GIMP!**_
- Instalación usando `dnf`:
```shell
sudo dnf install gimp
```
- Instalación usando flatpak:
```shell
flatpak install flathub org.gimp.GIMP
```
- También puedes instalarlo desde Discover.
---
## Git
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: Git es un sistema de control de versiones distribuido, gratuito y de código abierto, diseñado para gestionar todo tipo de proyectos con velocidad y eficiencia.
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://git-scm.com/download/linux
>
>![Image link|center|500](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/512px-Git-logo.svg.png)
### Instalación
```shell
sudo dnf install git
```
### Configurar
1. Poner nombre de usuario y correo
```shell
git config --global user.name "D4nivi"
git config --global user.email "danielvidalfajardo@gmail.com"
```
2. Instala [GitHub CLI](https://docs.github.com/es/get-started/getting-started-with-git/caching-your-github-credentials-in-git#github-cli):
```shell
sudo dnf install gh
```
3. Pon el siguiente comando y sigue los pasos:
```shell
gh auth login
```

>[!tip] Nota
>Si alguna vez te <span style="color:rgb(253, 253, 150)"><strong>pide introducir credenciales</strong></span> para pushear o clonar un repositorio tuyo y da <span style="color:rgb(255, 0, 0)"><strong>error</strong></span>, usa `gh auth refresh` para refrescar los credenciales.

---
## Java
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://developer.fedoraproject.org/tech/languages/java/java-installation.html
>![Image link|center|500](https://dungeonofbits.com/images/java-logo.png)
### Instalación
```shell
sudo dnf install java-devel java-openjdk
#java-openjdk deberia venir ya instalado con Fedora
```

---
## NerdFonts
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>GitHub</strong></span>: https://github.com/ryanoasis/nerd-fonts/tree/master
><span style="color:rgb(0, 209, 139)"><strong>Descargar Fuentes</strong></span>: https://www.nerdfonts.com/font-downloads
>
>![Image link|center|400](https://www.nerdfonts.com/assets/img/nerd-fonts-logo.svg)
### Instalación
- Para instalar una fuente, <span style="color:rgb(255, 192, 0)">descarga el .zip de la pagina de arriba</span> y <span style="color:rgb(0, 176, 80)">extrae</span> la carpeta (o una fuente en concreto) <span style="color:rgb(0, 176, 80)">en la carpeta</span> `~/.local/share/fonts` (si no existe la carpeta `fonts`, créala). Luego de eso, ejecuta el siguiente comando:
```shell
fc-cache -f
```
>[!info] ¿Qué hace este comando?
>_El comando <span style="color:rgb(253, 253, 150)"><strong>crea archivos de caché con información de la fuente</strong></span> para las aplicaciones. El parámetro <span style="color:rgb(217, 255, 26)"><strong>-f</strong></span> fuerza que se vuelvan a generar estos archivos, aunque estén actualizados._
### Cambiar Fuente de la Terminal
- Si usas <span class="rgb">Alacritty</span>, ve al <span style="color:rgb(0, 176, 80)">archivo de configuración</span> (debería estar en `~/.config/alacritty`), busca el apartado <span style="color:rgb(0, 176, 240)">fonts</span> y <span style="color:rgb(0, 176, 80)">escribe el nombre de la fuente en todos los apartados</span>. Si quieres usar una fuente <span style="color:rgb(0, 176, 240)">NerdFonts</span>, el nombre que debes poner es el que se ve en la página de descarga, con espacios y respetando las mayúsculas.

![[Alacritty fonts config.png|center]]

- Si usas <span style="color:rgb(0, 176, 80)">Konsole</span>, abre una terminal, dale a las <span style="color:rgb(0, 176, 80)">3 barras -> Preferencias -> Configurar Konsole -> Perfiles -> Nuevo -> Aspecto</span>. Escoge la nueva fuente a usar, aplica los cambios, guarda el perfil, selecciónalo como el predeterminado y reinicia Konsole.

---
## PyCharm
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: IDE para Python.
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://www.jetbrains.com/pycharm/download/?section=linux
><span style="color:rgb(0, 209, 139)"><strong>Pedir licencia para estudiantes</strong></span>: https://www.jetbrains.com/shop/eform/students
>
>![Image link|center|300](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/800px-PyCharm_Icon.svg.png)
### Instalación
Descarga el archivo comprimido de la pagina de <span style="color:rgb(0, 209, 139)"><strong>instalación</strong></span> y extráelo. La carpeta tendrá un archivo llamado `Install-Linux-tar.txt` con los <span style="color:rgb(1, 206, 225)"><strong>pasos para instalarlo</strong></span>.
- <span style="color:rgb(236, 54, 109)"><strong>Abre una terminal</strong></span> en la carpeta y pon el siguiente <span style="color:rgb(217, 255, 26)"><strong>comando</strong></span>:
```shell
./bin/pycharm.sh
```

<span style="color:rgb(255, 255, 0)"><strong>PyCharm</strong></span> se abrirá y se crearan los archivos de configuración. <span style="color:rgb(243, 119, 210)"><strong>Ya está listo para usar</strong></span>.

>[!note] Nota
><span style="color:rgb(255, 192, 0)"><strong>Reinicia PyCharm tras abrirlo con el comando</strong></span>, no se comporta como debería cuando se abre de esa manera.
### Configurar PyCharm
- Para poder abrir <span style="color:rgb(255, 255, 0)"><strong>PyCharm</strong></span> desde <span style="color:rgb(1, 206, 225)"><strong>cualquier lado en la terminal</strong></span>, añade la <span style="color:rgb(172, 79, 243)"><strong>ruta de la carpeta</strong></span> `bin` de la carpeta de instalación de <span style="color:rgb(255, 255, 0)"><strong>PyCharm</strong></span> al `$PATH`:
```txt title:"Dentro del ~/.zshrc"
export PATH=$PATH:/home/Danivi/Escritorio/Daniel/pycharm-2024.3/bin
```

- Para <span style="color:rgb(236, 54, 109)"><strong>instalar el idioma español</strong></span> (para evitar algunos <span style="color:rgb(0, 176, 80)"><strong>typos</strong></span>), ve a <span style="color:rgb(0, 209, 139)"><strong>File</strong></span> → <span style="color:rgb(0, 209, 139)"><strong>Settings ⚙</strong></span> → <span style="color:rgb(0, 209, 139)"><strong>Editor</strong></span> → <span style="color:rgb(0, 209, 139)"><strong>Natural Languages</strong></span>. Allí puedes añadir el idioma español.
‎ 
- Para poder <span style="color:rgb(255, 192, 0)"><strong>hacer zoom</strong></span> con el ratón, ve a <span style="color:rgb(0, 209, 139)"><strong>File</strong></span> → <span style="color:rgb(0, 209, 139)"><strong>Settings ⚙</strong></span> → <span style="color:rgb(0, 209, 139)"><strong>Editor</strong></span> → <span style="color:rgb(0, 209, 139)"><strong>General</strong></span>. Allí marca la <span style="color:rgb(18, 161, 217)"><strong>primera casilla</strong></span>. <u><strong><i>-Change font size with Ctrl+Mouse Wheel in: All editors-</i></strong></u>.

![[PyCharm zoom.png|center]]

---
## Spotify y Spicetify
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Requisitos</strong></span>: [`flathub`](https://flathub.org/setup)
><span style="color:rgb(0, 209, 139)"><strong>Instalar Spotify</strong></span>: https://docs.fedoraproject.org/en-US/quick-docs/installing-spotify/
><span style="color:rgb(0, 209, 139)"><strong>Instalar Spicetify</strong></span>: https://spicetify.app/docs/advanced-usage/installation
>
>![Image link|center|400](https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Spotify_logo_with_text.svg/2560px-Spotify_logo_with_text.svg.png)
>![Image link|center|500](https://i.imgur.com/iwcLITQ.png)
### Instalación Spotify
- Puedes instalar Spotify usando <span style="color:rgb(0, 176, 80)">flatpak</span>:
```shell
flatpak install flathub com.spotify.Client
```
En la página de instalación te da la opción de instalar usando rpm o snap. Te la pela, <span style="color:rgb(236, 54, 109)"><strong>instala siempre usando</strong></span> <span class="rgb">flatpak</span>.
### Instalación Spicetify
1. Primero <span style="color:rgb(0, 209, 139)"><strong><strong>damos permisos a los archivos de Spotify</strong></strong></span>. Copiamos la ruta donde se instaló Spotify y hacemos `sudo chmod a+wr`:
```shell
sudo chmod a+wr /var/lib/flatpak/app/com.spotify.Client/x86_64/stable/active/files/extra/share/spotify
sudo chmod a+wr /var/lib/flatpak/app/com.spotify.Client/x86_64/stable/active/files/extra/share/spotify/Apps -R
```
2. El siguiente comando <span style="color:rgb(0, 176, 80)">comenzará la instalación de Spicetify</span>:
```shell
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh
```
- Instala el <span style="color:rgb(255, 192, 0)"><strong>Marketplace</strong></span> si te lo pide, te dará <span style="color:rgb(255, 0, 0)"><strong>error</strong></span>, es normal.
3. Ve a `~/.config/spicetify` y edita el archivo `config-xpui.ini`. Dentro del archivo:
	- Comprueba que el <span style="color:rgb(0, 176, 80)">spotify-path</span> es correcto (la ruta debe ser la que usamos antes con el comando `chmod`).
	‎ 
	- Añade (si no lo está) el <span style="color:rgb(0, 176, 80)">prefs-path</span>. Compruébalo, pero debería ser `/home/usuario/.var/app/com.spotify.Client/config/spotify/prefs`. 
	‎ 
	- <span style="color:rgb(255, 136, 0)">Si no existe</span>, abre Spotify (<span style="color:rgb(0, 176, 80)">la carpeta</span> `com.spotify.Client` <span style="color:rgb(0, 176, 80)">se crea al abrir Spotify</span>). <span style="color:rgb(255, 192, 0)">Si no se crea</span>, entonces la ruta debe ser `/home/usuario/.config/spotify/prefs`.

![[Spicetify config.png|center]]

>[!danger] Importante 
>El <span style="color:rgb(0, 209, 139)"><strong><strong>prefs\_path</strong></strong></span> debe ser una ruta absoluta, no podemos usar <span style="color:rgb(217, 255, 26)"><strong>~</strong></span>. Al editar el archivo de configuración, simplemente cambia `usuario` por tu nombre de usuario._

4. <span style="color:rgb(0, 176, 240)">Ve a una nueva terminal</span>, pon el comando de instalación de nuevo e instala el <span style="color:rgb(255, 192, 0)"><strong>Marketplace</strong></span>. 
- Si da error porque <span style="color:rgb(0, 176, 80)">no detecta el comando</span> <span style="color:rgb(0, 176, 80)">Spicetify</span>, es porque no estas usando una nueva sesión de terminal (o no se ha instalado bien, cosa que no debería suceder).
- Si da error por `permiso denegado`, seguramente sea por no haber puesto los comandos del <span style="color:rgb(236, 54, 109)"><strong>apartado 1</strong></span>. 
- Si el error anterior da tras actualizar <span style="color:rgb(255, 192, 0)"><strong>Spicetify</strong></span>, <span style="color:rgb(0, 209, 139)"><strong><strong>reinstala Spotify</strong></strong></span>. Para desinstalarlo, usa:
```shell
sudo flatpak remove spotify
```

---
## VirtualBox
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Requisitos</strong></span>: [`rpm`](https://rpmfusion.org/Configuration)
><span style="color:rgb(0, 209, 139)"><strong>Web Oficial</strong></span>: https://www.virtualbox.org/wiki/Downloads
><span style="color:rgb(0, 209, 139)"><strong><strong>Instalación</strong></strong></span>: https://rpmfusion.org/Howto/VirtualBox
><span style="color:rgb(0, 209, 139)"><strong><strong>Máquina Virtual Fedora 32</strong></strong></span>: https://ditec.um.es/iso/
>
>![Image link|center|250](https://upload.wikimedia.org/wikipedia/commons/d/d5/Virtualbox_logo.png)
### Instalación
Para instalar <span style="color:rgb(18, 161, 217)"><strong>VirtualBox</strong></span>, sigue los pasos de <span style="color:rgb(0, 209, 139)"><strong><strong>Instalación</strong></strong></span>:
1. Instalar con `dnf`:
```shell
sudo dnf install VirtualBox
```
2. Ejecuta el script `akmods`:
```shell
sudo akmods
sudo systemctl restart vboxdrv
lsmod  | grep -i vbox          # comprobación de que ha funcionado
```
3. Instala el <span style="color:rgb(236, 54, 109)"><strong>Oracle VM VirtualBox Extension Pack</strong></span> de la <span style="color:rgb(0, 209, 139)"><strong><strong>Web Oficial</strong></strong></span>.
![[VirtualBox descarga.png|center|700]]

- Puede que al abrir aparezca un <span style="color:rgb(225, 71, 71)"><strong>error</strong></span> que diga "<span style="color:rgb(217, 255, 26)"><strong><i>No se pueden enumerar los dispositivos USB</i></strong></span>". Para resolverlo, te pedirá que añadas el usuario al grupo `vboxusers`:
```shell
sudo usermod -aG vboxusers Danivi
```
- <span style="color:rgb(243, 119, 210)"><strong>Reinicia</strong></span> para que deje de salir el error.

<span style="color:rgb(255, 192, 0)"><strong>Antes de poder arrancar máquinas virtuales</strong></span>, necesitamos hacer unos arreglos. Los <span style="color:rgb(1, 206, 225)"><strong>pasos a seguir</strong></span> se pueden consultar en `/usr/share/doc/akmods/README.secureboot`.
```shell
sudo /usr/sbin/kmodgenca -a
mokutil --import /etc/pki/akmods/certs/public_key.der 
# El comando pedirá contraseña, usa password (la usarás más tarde)
```
- Tras poner estos comandos, <span style="color:rgb(0, 209, 139)"><strong><strong>reinicia</strong></strong></span>. Antes de entrar al menú de GRUB te encontrarás una pantalla como esta, selecciona `Enroll MOK` → `Continue` → `Yes` y pon la contraseña.

![[VirtualBox Enroll MOK.png|center|600]]

Tras esto vuelves a Fedora. <span style="color:rgb(255, 192, 0)"><strong>Pon el siguiente comando para comprobar que ha funcionado</strong></span>:
```shell
mokutil --test-key /etc/pki/akmods/certs/public_key.der
# La salida debería ser algo como esto:
# /etc/pki/akmods/certs/public_key.der is already enrolled
```
---
## Visual Studio Code
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Requisitos</strong></span>: [`rpm`](https://rpmfusion.org/Configuration)
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://code.visualstudio.com/docs/setup/linux
>
>![Image link|center|250](https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/visual-studio-code-icon.png)
### Instalación
1. Importamos el repositorio y la llave:
```shell
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null
```

2. Actualizamos la caché del paquete y lo instalamos con `dnf`:
```shell
dnf check-update
sudo dnf install code
```

>[!tip] Nota 
>_Al parecer el depurador viene con Fedora, no hizo falta instalar nada._

---
## VLC
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Requisitos</strong></span>: [`rpm`](https://rpmfusion.org/Configuration)
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://www.videolan.org/vlc/
>
>![Image link|center|270](https://upload.wikimedia.org/wikipedia/commons/3/38/VLC_icon.png)
### Instalación
- Puedes instalarlo, si tienes los repositorios de rpm, con `dnf`:
```shell
sudo dnf install vlc
```
- También puede ser instalado desde la <span style="color:rgb(255, 192, 0)">tienda de KDE</span> (<span style="color:rgb(255, 192, 0)">Discover</span>) o cualquier otra tienda.

![[vlc discover.png|center|650]]
Recuerda poner <span style="color:rgb(255, 192, 0)">VLC</span> como el <span style="color:rgb(255, 192, 0)">reproductor de video predeterminado</span>, en Fedora, se puede hacer en <span style="color:rgb(0, 176, 80)">Preferencias del sistema -> Aplicaciones predeterminadas</span>.

---
## WhatsApp
>[!danger] Obsoleto
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: Wasaaaaaaaaaaaaa
><span style="color:rgb(0, 209, 139)"><strong>Requisitos</strong></span>: [`flathub`](https://flathub.org/setup)
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://flathub.org/apps/io.github.mimbrero.WhatsAppDesktop
>![Image link|center|300](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1024px-WhatsApp.svg.png)
### Instalación
<span style="color:rgb(236, 54, 109)"><strong>La aplicación ya no está disponible</strong></span>, habrá que buscar otra alternativa cuando sea necesario.

---
## Wine
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: Permite correr aplicaciones de Windows en Linux.
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://www.youtube.com/watch?v=OOQDdwpWvyQ
>![Image link|center|200](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/WINE-logo.svg/1200px-WINE-logo.svg.png)
### Instalación
- Primero instalamos <span style="color:rgb(236, 54, 109)"><strong>Wine</strong></span>:
```shell
sudo dnf install winetricks
```
- Tras instalarlo, ponemos el siguiente comando en la terminal para crear la <span style="color:rgb(253, 253, 150)"><strong>carpeta de configuración</strong></span> de Wine (.wine, se crea en el `$HOME`):
```sh
wineboot
```
### ¿Cómo usar Wine?
- Para <span style="color:rgb(243, 119, 210)"><strong>abrir aplicaciones con Wine</strong></span>, simplemente hacemos <span style="color:rgb(0, 176, 80)"><strong>click derecho en la aplicación</strong></span> y debería aparecer la siguiente opción:
![[Wine abrir aplicaciones.png|center]]
‎ 
- También puedes usar el <span style="color:rgb(217, 255, 26)"><strong>comando</strong></span> `wine`:
```sh
wine DLXide.exe
```

---
## XClicker
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: autoclicker para Linux (como el de Windows pero en modo oscuro).
>
><span style="color:rgb(0, 209, 139)"><strong>Página oficial</strong></span>: https://xclicker.xyz/
><span style="color:rgb(0, 209, 139)"><strong>Guía de instalación</strong></span>: https://github.com/robiot/xclicker/wiki/Installation
>
>![Image link|center|150](https://dl.flathub.org/repo/appstream/x86_64/icons/128x128/xyz.xclicker.xclicker.png)
### Instalación
1. Ve la la <span style="color:rgb(0, 209, 139)"><strong>Página oficial</strong></span> y descarga e instala la última versión (en `.AppImage`). 

2. Ahora ve a la carpeta de descarga, abre una terminal y pon el siguiente comando:
```sh
chmod +x ./*.AppImage
```

3. Añade el programa al menú de KDE. Usa la imagen de aquí.

---
## zsh
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: <span style="color:rgb(1, 206, 225)"><strong>zsh</strong></span> es un intérprete de comandos (_shell_) para sistemas operativos Unix. <span class="rgb">ohmyzsh</span> es un framework para administrar la configuración de <span style="color:rgb(1, 206, 225)"><strong>zsh</strong></span>, que incluye miles de funciones útiles, plugins, temas, etc.
>
><span style="color:rgb(0, 209, 139)"><strong>Instalar zsh</strong></span>: https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH
><span style="color:rgb(0, 209, 139)"><strong>Instalar ohmyzsh</strong></span>: https://ohmyz.sh
><span style="color:rgb(0, 209, 139)"><strong>Temas</strong></span>: https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
><span style="color:rgb(0, 209, 139)"><strong>Plugins</strong></span>: https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins
><span style="color:rgb(0, 209, 139)"><strong>Mis plugins</strong></span>: https://gist.github.com/n1snt/454b879b8f0b7995740ae04c5fb5b7df
>
>![Image link|center|500](https://ohmyzsh.s3.amazonaws.com/omz-ansi-github.png)
### Instalación zsh
1. Instala el programa con `dnf`:
```shell
sudo dnf install zsh
```
2. Añade zsh a la lista de shells autorizadas. Para ver si ya lo está, el path al ejecutable de zsh debería estar en `/etc/shells`. Edita el archivo para comprobarlo:
```shell
sudo nano /etc/shells
```
![[zsh shells.png]]

Si no está, añádelo. Puedes ver el path del ejecutable de zsh con:
```shell
which zsh   # Debería devolver /usr/bin/zsh
```
3. Pon a <span style="color:rgb(0, 176, 80)">zsh</span> como tu shell predeterminada. 
```shell
chsh -s $(which zsh)
```
4. <span style="color:rgb(255, 136, 0)">Reinicia</span>. Tras el reinicio, abre una terminal, debería aparecer un mensaje como éste. <span style="color:rgb(0, 176, 240)">Usa la opción 0</span>, esto creará el <span style="color:rgb(0, 176, 80)">archivo de configuración</span> `.zshrc` en el home.
![[startup zsh.png]]
### Instalación ohmyzsh
```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
- Al ejecutar el comando, debería aparecer un mensaje así en la terminal, lo que significa que el programa se ha instalado correctamente:
![Image link|center](https://terminaldelinux.com/terminal/preparacion-entorno/instalacion-zsh/oh-my-zsh-install.png)
### Plugins y Temas
- Para añadir <span style="color:rgb(0, 176, 80)">plugins</span> a zsh, lo único que tienes que hacer es <span style="color:rgb(0, 176, 80)">añadir el nombre del plugin</span> a la línea `plugins` del archivo de configuración, <span style="color:rgb(0, 176, 240)">separados por espacios</span> (<span style="color:rgb(225, 71, 71)">no uses comas</span>).

![[zsh plugins.png|center]]

>[!danger] Importante 
>_Hay ciertos <span style="color:rgb(0, 176, 240)"><i>plugins</i></span> que <span style="color:rgb(0, 176, 240)"><i>no están en el repositorio de zsh</i></span>, y que deben ser <span style="color:rgb(0, 176, 240)"><i>instalados</i></span> primero antes de ser añadidos al archivo de configuración. Es el caso de los plugins_ `zsh-autosuggestions`, `zsh-syntax-highlighting`, `zsh-fast-syntax-highlighting` _y_ `zsh-autocomplete`.

- Si quieres instalar mis plugins, ejecuta los siguientes comandos:
```shell
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
```
- Y cambia la línea de plugins del archivo de configuración por esta:
```text title:"Dentro del ~/.zshrc"
plugins=(git zsh-autosuggestions zsh-syntax-highlighting fast-syntax-highlighting zsh-autocomplete)
```
- Para instalar <span style="color:rgb(0, 176, 80)">temas</span>, simplemente busca la línea `ZSH_THEME` en el archivo de configuración y <span style="color:rgb(0, 176, 80)">escribe el nombre del tema</span> que quieras usar. En mi caso, uso <span style="color:rgb(225, 71, 71)">"bira"</span>.

![[zsh theme.png|center]]

---
## _Utilidades Terminal_
## bat
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: comando ``cat`` tuneado, con syntax highlighting y otras muchas opciones.
><span style="color:rgb(0, 209, 139)"><strong>GitHub</strong></span>: https://github.com/sharkdp/bat
>
>![Image link|center|500](https://camo.githubusercontent.com/be35879c510cea3111901d01e4af4d7e8f38fbb7c56a49ca711f07edf1b2d6fd/68747470733a2f2f696d6775722e636f6d2f724773646e44652e706e67)
### Instalación
```shell
sudo dnf install bat
```

---
## btop
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: comando `top` tuneado.
><span style="color:rgb(0, 209, 139)"><strong>GitHub</strong></span>: https://github.com/aristocratos/btop
>
>![Image link|center|600](https://github.com/aristocratos/btop/raw/main/Img/normal.png)
### Instalación
```sh
sudo dnf install btop
```

---
## brightnessctl
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: comando de terminal que te permite cambiar el nivel de brillo.
><span style="color:rgb(0, 209, 139)"><strong>GitHub</strong></span>: https://github.com/Hummer12007/brightnessctl?tab=readme-ov-file
>
>![[brightnessctl.png|center|500]]
>![[brightnessctl brillo actualizado.png|center|500]]
### Instalación
```shell
sudo dnf install brightnessctl
```
### Cambiar el nivel de brillo
- Poner `brightnessctl` <span style="color:rgb(253, 253, 150)">solo te dice el nivel de brillo</span> (en porcentaje).
- <span style="color:rgb(253, 253, 150)">Para cambiar el nivel de brillo</span>, usas `brightnessctl set brillo%`:
```shell
brightnessctl set 100%
```

---
## CMake
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: CMake es un software multiplataforma diseñado para la compilación automatizada en varios sistemas operativos.
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://developer.fedoraproject.org/tech/languages/c/cmake.html
>
>![Image link|center|500](https://e3sm.org/wp-content/uploads/2019/10/CMake-logo-l.png)
### Instalación
```shell
sudo dnf install cmake
```

---
## dpkg (Debian Package)
>[!Info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: comando que se utiliza para instalar, desinstalar, y proporcionar información sobre los paquetes. Es la base del sistema de gestión de paquetes de Debian.
><span style="color:rgb(0, 209, 139)"><strong>Más información</strong></span>: https://keepcoding.io/blog/que-es-el-comando-dpkg-en-linux
>![Image link|center](https://i0.wp.com/www.admin-cassos.fr/wp-content/uploads/2023/03/dpkg.png?fit=256%2C256&ssl=1)
### Instalación
```shell
sudo dnf install dpkg
```

---
## htop
>[!Info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: comando [[4. Comandos Control de Recursos#4.5 top | top]] tuneado con colorines.
><span style="color:rgb(0, 209, 139)"><strong>Web oficial</strong></span>: https://htop.dev
>
>![Image link|center|600](https://htop.dev/images/htop-2.0.png)
### Instalación
```shell
sudo dnf install htop
```

---
## lsd
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: ls mejorado con colores, iconos y temas disponibles.
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://github.com/lsd-rs/lsd
><span style="color:rgb(0, 209, 139)"><strong>Ayuda instalación temas</strong></span>: https://draculatheme.com/lsd
>
>![Image link|center|500](https://i.ytimg.com/vi/6MlOaZ_KgxA/maxresdefault.jpg)
### Instalación
1. Instala <span class="rgb">lsd</span> con `dnf`:
```shell
sudo dnf install lsd
```
2. Opcionalmente, puedes crear un <span style="color:rgb(243, 119, 210)"><i>alias</i></span> para <span class="rgb">lsd</span>, sustituyendo el comando ls por lsd. Para ello, en el archivo `~/.bashrc` ó `~/.zshrc` (dependiendo de cual uses) busca el apartado de alias y añade la siguiente línea:
```text
alias ls='lsd'
```
![[lsd alias.png|center]]
Para más información acerca de los alias, ver [[Alias en Linux]].
#### Temas
 Tras la instalación, si no se crea una carpeta llamada `lsd` en `~/.config`, créala.
```shell
cd ~/.config
mkdir lsd
```
- Descarga [éste]() zip. Contiene 3 archivos:
	- El archivo de configuración `config.yaml`
	- Un archivo que hace que todo funcione `colors.yaml`
	- El tema de dracula, `dracula.yaml`. 
- Mueve los archivos a la carpeta de `lsd` que acabas de crear. Para que el tema funcione, <span style="color:rgb(0, 176, 80)">asegúrate de que en el archivo</span> `config.yaml` <span style="color:rgb(0, 176, 80)">el tema sea</span> <span style="color:rgb(0, 176, 240)">custom</span>.

![[lsd theme.png|center]]

---
## lshw
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: Herramienta que muestra información detallada sobre el hardware de la maquina.
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://packages.fedoraproject.org/pkgs/lshw/lshw/
><span style="color:rgb(0, 209, 139)"><strong>Opciones del comando</strong></span>: Ver _[[5. Comandos Entrada_Salida#5.11 lshw | Comando lshw]]_.
>
>![Image link|center|500](https://aodatacloud.es/wp-content/uploads/2024/02/hardware.png)
#### Instalación
```shell
sudo dnf install lshw
```

---
## neofetch
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: Herramienta que muestra información sobre el sistema operativo, software y hardware de una manera estética y visualmente agradable.
><span style="color:rgb(0, 209, 139)"><strong>GitHub</strong></span>: https://github.com/dylanaraps/neofetch
>
>![Image link|center|500](https://camo.githubusercontent.com/9c9040bf40c25e9787f68937aa33c5057816e35e39e467749d0f220c9a6da8ac/68747470733a2f2f692e696d6775722e636f6d2f5a51493245597a2e706e67)
### Instalación
```shell
sudo dnf install neofetch
```

---
## nvtop
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: comando `top` pero para uso de la GPU.
><span style="color:rgb(0, 209, 139)"><strong>GitHub</strong></span>: https://github.com/Syllo/nvtop
>
>![Image link|center](https://github.com/Syllo/nvtop/raw/master/screenshot/NVTOP_ex1.png)
### Instalación
```shell
sudo dnf install nvtop
```

---
## pip
>[!Info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: pip es el package manager de Python. Lo usas para instalar librerías externas.
><span style="color:rgb(0, 209, 139)"><strong>Instalación</strong></span>: https://developer.fedoraproject.org/tech/languages/python/pypi-installation.html
>
>![Image link|center](https://www.telecomhall.net/uploads/db2683/original/2X/9/93768e7290bc8c8473a02561ac4e608642cfbaca.png)
### Instalación
- Podemos instalar <span style="color:rgb(255, 255, 0)"><strong><i>pip</i></strong></span> para usuario usando `dnf`:
```shell
sudo dnf install pyhton3-pip
```
- Cuando instalemos un paquete con <span style="color:rgb(255, 255, 0)"><strong><i>pip</i></strong></span>, los ejecutables se guardarán en `~/.local/bin`, por lo que deberemos añadir esta carpeta a `$PATH`. Para ello, ve al archivo `~/.bashrc` ó `~/.zshrc` (dependiendo de cual uses) y añade esta línea:
```shell
export PATH=$PATH:/home/usuario/.local/bin   
# cambia usuario por tu nombre de usuario
```
- Los paquetes que instales con <span style="color:rgb(255, 255, 0)"><strong><i>pip</i></strong></span> deben actualizarse a mano, no se actualizaran con `dnf`. Para ello, pon este comando:
```shell
pip install update
```

---
## yt-dlp
>[!info]
><span style="color:rgb(0, 209, 139)"><strong>Descripción</strong></span>: Programa de terminal para descargar videos de YouTube.
><span style="color:rgb(0, 209, 139)"><strong>GitHub</strong></span>: https://github.com/yt-dlp/yt-dlp
><span style="color:rgb(0, 209, 139)"><strong>Comandos</strong></span>: https://atareao.es/podcast/yt-dlp-es-una-pura-maravilla-eliminando-carazas/
><span style="color:rgb(0, 209, 139)"><strong>Descargar videos de cualquier página</strong></span>: https://joangabriel.medium.com/como-descargar-v%C3%ADdeos-desde-cualquier-sitio-web-usando-linux-25dca64e48a5
>
>![Image link](https://raw.githubusercontent.com/yt-dlp/yt-dlp/master/.github/banner.svg)

### Instalación
- Es altamente recomendado instalar [ffmpeg](https://www.ffmpeg.org):
```shell
sudo dnf install ffmpeg
```
>[!tip] Nota 
>_Si hay <span style="color:rgb(236, 54, 109)"><strong>conflicto entre paquetes</strong></span>, añade la opción <span style="color:rgb(217, 255, 26)"><strong>--allowerasing</strong></span> al comando._

- Para instalar <span style="color:rgb(0, 209, 139)"><strong><strong>yt-dlp</strong></strong></span>, podemos usar `dnf`:
```shell
sudo dnf install yt-dlp
```
### ¿Cómo usar?
- Descargar <span style="color:rgb(0, 209, 139)"><strong>video</strong></span> o <span style="color:rgb(0, 209, 139)"><strong>playlist</strong></span> en la <span style="color:rgb(0, 209, 139)"><strong>mejor calidad</strong></span>:
```shell
yt-dlp "URL"
```
- Descargar <span style="color:rgb(0, 209, 139)"><strong>audio</strong></span>:
```shell
yt-dlp -x --audio-format mp3 "URL"  # mp3 puede ser cambiado por otro formato
```
- Descargar <span style="color:rgb(0, 209, 139)"><strong>fragmento de un vídeo</strong></span>:
```shell
yt-dlp "URL" --download-sections "*INICIO-FINAL" --force-keyframes-at-cuts
# INICIO y FINAL es el tiempo de inicio y final del clip, en segundos
```
- Descargar <span style="color:rgb(0, 209, 139)"><strong>video con subtítulos incrustados</strong></span>:
```shell
yt-dlp --write-sub --sub-lang LANG "URL"
```
- <span style="color:rgb(0, 209, 139)"><strong>Ver formatos</strong></span> en los que se puede descargar el video:
```shell
yt-dlp -F "URL"
```
- Descargar <span style="color:rgb(0, 209, 139)"><strong>video con formato especificado</strong></span> (puede ser un <span style="color:rgb(0, 176, 240)">formato</span> como mp4, webm, etc, o puede ser el <span style="color:rgb(0, 176, 240)">nsv</span>, un <span style="color:rgb(0, 176, 240)">número asociado al formato</span>, visto al usar `yt-dlp -F "URL"`):
```shell
yt-dlp -f FORMATO "URL"
```

---
