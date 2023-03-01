from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QPushButton, QStyleOptionButton, QStyle


class HRoundedButton(QPushButton):
    def __init__(self, text: str, parent: QPushButton = None) -> None:
        super().__init__(text, parent)
        # self.setStyleSheet()
