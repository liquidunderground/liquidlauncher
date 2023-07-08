ifeq ($(OS), Windows_NT)
ENTER_VENV :=./.venv/bin/activate.ps1
EXIT_VENV :=./.venv/bin/deactivate.ps1
ICON_FLAG := --windows-icon-from-ico=img/icons/ll.ico
else ifeq ($(OS), Darwin)
ICON_FLAG := --macos-app-icon=img/icons/ll.ico
ENTER_VENV :=. ./.venv/bin/activate
EXIT_VENV :=. ./.venv/bin/deactivate
else
ENTER_VENV :=. ./.venv/bin/activate
EXIT_VENV :=. ./.venv/bin/deactivate
ICON_FLAG := --linux-icon=img/icons/ll.ico 
endif

NUITKA_FLAGS := --output-dir=dist/ ${ICON_FLAG} --standalone --onefile --disable-console
NUITKA_PLUGINS := --enable-plugin=pyside6,anti-bloat,pywebview
NUITKA_PACKAGES := --include-package=xml.sax

.PHONY: all init run dist clean

all:
	@echo -e "USAGE:\n\n"\
	"dist: create distributable build\n"\
	"init: initialize virtual environment\n"\
	"run: run development build directly\n"\
	"clean: clean up your environment\n"

# Run a shell that does all the things
init: requirements.txt
	 test -d ./.venv || python3 -m venv ./.venv
	( if [[ -z "$(VIRTUAL_ENV)" ]]; then $(ENTER_VENV); fi && pip install -r requirements.txt )

ll_ui.py: init
	if [[ -z "$(VIRTUAL_ENV)" ]]; then $(ENTER_VENV); fi && pyside6-uic ll.ui -o ll_ui.py 

ll_rc.py: init
	if [[ -z "$(VIRTUAL_ENV)" ]]; then $(ENTER_VENV); fi && pyside6-rcc ll.qrc -o ll_rc.py

run: init
	( if [[ -z "$(VIRTUAL_ENV)" ]]; then $(ENTER_VENV); fi && python3 ll_main.py )

dist: init
	( if [[ -z "$(VIRTUAL_ENV)" ]]; then $(ENTER_VENV); fi && nuitka3 ll_main.py ${NUITKA_FLAGS} ${NUITKA_PLUGINS} ${NUITKA_PACKAGES} --output-filename=LiquidLauncher )

clean:
	-rm -r build/ dist/ ll_main.spec .venv/ ll_profiles

