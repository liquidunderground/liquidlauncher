![LiquidLauncher logo](img/liquidlauncher.svg)

LiquidLauncher
==============

### This fork has the following features:

- A master server browser. You can view online SRB2 servers and select one to join.
- A mod browser and installer. See a list of mods from the SRB2 message board, and click a button to download them.
- Support for multiple settings profiles.
- Settings and profiles are saved as easily editable TOML files (similar to INI files).
- Multithreading, to avoid GUI freezing.

![](ms_list_screenshot.png)

![](mod_downloader_screenshot.png)


Features
--------

### Inherited from LauncherBlast2

- Settings profile manager
- Launch option manager
    - Game settings manager
    - Mod inclusion manager
- Basic Netgame manager
- Basic Master Server browser
- Multithreaded network queries
- Newsfeed

### What we added

- Overhauled netgame browser system (*heavily* modified to improve UI and extend it's features)
    - Port-aware distinction of netgames
- Support for multiple master servers. Supported APIs:
    - Vanilla SRB2 ("v1")
    - SRB2Kart Master Server
    - LiquidMS Snitch
- Support for alternative mod browser sources:
    - Workshop Blue Sphere (*use at your own risk*)
    - Workshop Red Sphere (**non-compliant to SRB2MB standards**)
    - Reworked Message Board query logic
- **Planned:** Support for multiple RSS feeds
- ~~Ability to host on varying master servers~~ *Blocked by lack of launch flag*

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

`netgames.json`
: Your bookmarked netgames.

`masterservers.toml`
: Your saved master servers. By default, these are filled in with the official

  STJr and Kart Krew master servers.
