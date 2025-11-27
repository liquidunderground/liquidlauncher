### Cheat code functions ###

def gotoPage(cheat:str, page=None):
    if page == None:
        pass
    ui.SettingsStackedWidget.setCurrentWidget(page)
    pass

### Cheat code map ###
def run_cheat(cheat:str, ui):

    f_cheats = {
        "418imateapot": ui.HttpSettingsPage,
        "ms": ui.MSSettingsPage,
        "masterserver": ui.MSSettingsPage,
        "masterservers": ui.MSSettingsPage,
        "rss": ui.RSSSettingsPage,
        "unclesonic": ui.ModSourcesSettingsPage,
    }


    realcheat = ''.join(cheat.lower().split())

    if realcheat in f_cheats:
        
        ui.SettingsStackedWidget.setCurrentWidget(f_cheats[realcheat])
        return