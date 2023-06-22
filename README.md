![LiquidLauncher logo](img/liquidlauncher.svg)

LiquidLauncher
==============

Features
--------

This Launcher is forked from [HitCoder9768's LauncherBlast2-reBoot](https://github.com/HitCoder9768/LauncherBlast2-reBoot).
As such, This section is gonna be divided into three parts, distinguished
by the forks responsible for the changes:


### LiquidLauncher additions

#### Fully featured RSS/Atom newsreader

![Newsreader view](img/scr_news.png)

- *Massive* UI overhaul
- support for multiple news sources

#### Overhauled netgame browser system (*heavily* modified to improve UI and extend it's features)

![Bookmarked netgames view](img/scr_masterserver.png)

- Port-aware distinction of netgames
- Support for multiple master servers. Supported APIs:
    - Vanilla SRB2 ("v1")
    - SRB2Kart Master Server ("kartv2")
    - [LiquidMS] [Snitch] ("snitch")
- ~~Ability to host on different master servers~~ *Blocked by lack of launch flag*


[LiquidMS]: <https://github.com/zibonbadi/liquidms>
[Snitch]: <https://github.com/zibonbadi/liquidms/blob/main/doc/reference/snitch.md>

#### Support for alternative mod browser sources (*use at your own risk*)

![Mod browser view](img/scr_modbrowser.png)

- Reworked Message Board query logic
- SRB2 Workshop Blue Sphere support 
- SRB2 Workshop Red Sphere support (**non-compliant to SRB2MB standards**)
- *Planned:* SRB2 WAD Archive support
- *Planned:* SRB2 Gamebanana support
- *Planned:* SRB2 Skybase support

### Inherited from HitCoder9768's fork

- A master server browser. You can view online SRB2 servers and select one to join.
- A mod browser and installer. See a list of mods from the SRB2 message board, and click a button to download them.
- Support for multiple settings profiles.
- Settings and profiles are saved as easily editable TOML files (similar to INI files).
- Multithreading, to avoid GUI freezing.


### Inherited from Classic LauncherBlast2

- Settings profile manager
- Launch option manager
    - Game settings manager
    - Mod inclusion manager
- Basic Netgame manager ()
- Basic Master Server browser (only supported STJr and Kart Krew servers before)
- Multithreaded network queries
- Basic Newsfeed integration (single source; <https://mb.srb2.org/feed>)


Installation
------------

### Windows

Simply put `liquidlauncher.exe` into your SRB2 directory. This should make sure
that all commands run by LiquidLauncher point to the right files.

#### A note on antivirus

Many modern antivirus solutions check against a database of known file
hashes, which can lead to false positives for lesser-known homebrew
projects such as this.

Of course, we'd like you to verify our launcher using another antivirus
scan such as [VirusTotal], but unless there's been a middleman inbetween
you and the GitHub servers (which HTTPS should prevent), our executables
contain no malware and should be safe to execute. Please don't run them as
administrator though, it's not necessary.

[VirusTotal]: <https://www.virustotal.com>

### Linux

Just run it. Linux usually installs the game globally and resolves file lookup
itself, so it doesn't matter.

If you run the Flatpak version... send us your issues and we'll seek to fix
them :3

### Building for developers

[PyInstaller] is already included in our `requirements.txt` simply install it
into your (virtual) environment and run the following command:

[PyInstaller]: <https://pypi.org/project/pyinstaller/>

   user$ pyinstaller ll_main.py --icon=img/icons/ll.ico --onefile --windowed


CONTRIBUTING
------------

Here's a quick breakdown of our tools:

### Python

LiquidLauncher is written in Python. In order to start developing
LiquidLauncher, we recommend using our make recipe:

    user$ make init

Alternatively, you can also manually [set up a virtual environment][PyVEnv].

[PyVEnv]: <https://docs.python.org/3/library/venv.html>

    user$ python3 -m venv /path/to/new/virtual/environment

After that's done, install the necessary packages into there.

    user$ pip install -r requirements.txt

In order to run your development builds, use Python 3:

    user$ python3 ll_main.py


### Qt UI and Resources

The graphical interface is done using Qt Designer. To generate a compiled
Python BLOB, simply run the respective Qt compilers:

    user$ pyside6-uic ll.ui -o ll_ui.py
    user$ pyside6-rcc ll.qrc -o ll_rc.py

Alternatively, we've also supplied Make recipies to do this:

    user$ make ll_ui.py
    user$ make ll_rc.py

Due to Qt requirements, resource images are to be included in PNG format.
For editing, please use SVG if you can (this will future-proof the graphics).  
Icons are rendered/exported with a standard height of 64px.

`default.html` is a resource to be included in `ll.qrc`. It provides the
initial page for the RSS browser.


### Distributable builds

Distributable builds are done using [PyInstaller] and we prefer one-file
builds for easy distribution. Here's the command to do it.

   user$ pyinstaller ll_main.py --icon=img/icons/ll.ico --onefile --windowed

We also defined a `make` recipe for your convenience:

   user$ make dist



What are all those files?
-------------------------

On first launch, LiquidLauncher will create a few config files to help. These
are largely in TOML format and should be fairly easy to exchange and edit.

`ll_profiles/default.toml`
: A default game profile. You can create additonal profiles under `Game -> Profiles`

`settings.toml`
: Global settings. This includes your current profile, available profiles, mod
sources (also your RSS feeds someday) and your currently selected Master Server

`netgames.toml`
: Your bookmarked netgames.

`masterservers.toml`
: Your saved master servers. By default, these are filled in with the official

  STJr and Kart Krew master servers.
