#!/bin/sh
. ./.venv/bin/activate
pyinstaller -y spec/hQtWidget.spec
deactivate