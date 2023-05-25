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


What are all those files?
-------------------------

On first launch, LiquidLauncher will create a few config files to help. These
are largely in TOML format and should be fairly easy to exchange and edit.

`default_profile.toml`
: A default game profile. You can create additonal profiles under `Game -> Profiles`

`settings.toml`
: Global settings. This includes your current profile, available profiles, mod
sources (also your RSS feeds someday) and your currently selected Master Server

`netgames.toml`
: Your bookmarked netgames.

`masterservers.toml`
: Your saved master servers. By default, these are filled in with the official

  STJr and Kart Krew master servers.
