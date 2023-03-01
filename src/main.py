import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class HApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self._init_ui()

    def _init_ui(self):

        # Main UI
        self.setWindowTitle("HApp")
        self.show()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        ex = HApp()
        sys.exit(app.exec())
    except Exception as ex:
        print(ex)
