### Cheat code functions ###

def unlockHttpSettings(cheat:str, ui):
    ui.devSettingsStackedWidget.setCurrentWidget(ui.httpDevPage)
    pass

def unlockModsources(cheat:str, ui):
    ui.devSettingsStackedWidget.setCurrentWidget(ui.modsourcesDevPage)
    pass

def _fallback(cheat:str, ui):
    # Do whatever we need to in case there's no match
    ui.devSettingsStackedWidget.hide()
    pass


### Cheat code map ###

f_cheats = {
    "418imateapot": unlockHttpSettings,
    "unclesonic": unlockModsources,
}

def run_cheat(cheat:str, ui):
    realcheat = ''.join(cheat.lower().split())

    if realcheat in f_cheats:
        ui.devSettingsStackedWidget.show()
        #ui.devSettingsStackedWidget.setEnabled(True)
        f_cheats[realcheat](cheat, ui)
        return
    _fallback(realcheat, ui)