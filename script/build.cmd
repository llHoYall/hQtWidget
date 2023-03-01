@ECHO Off
CALL ./.venv/Scripts/activate
pyinstaller -y spec/hQtWidget.spec
CALL deactivate