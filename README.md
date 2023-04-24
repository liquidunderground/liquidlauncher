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
- ~~Ability to host on varying master servers~~ *Blocked by lack of launch flag*

Installation
------------

TBA. For a dev build, just launch `ll_main.py` through Python
