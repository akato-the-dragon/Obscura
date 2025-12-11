from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QDialog, QWidget, QMainWindow


class Dimmer(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setPalette(QColor(0, 0, 0, 128))
        self.setAutoFillBackground(True)
        self.setGeometry(parent.rect())
        self.setWindowFlag(Qt.FramelessWindowHint)
    
    def update_geometry(self) -> None:
        self.setGeometry(self.parent().rect())


class CorePopup(QDialog):
    def __init__(self, parent: QMainWindow):
        super().__init__(parent)

        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.Popup)
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowTitleHint, False)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setColor(QColor(0,0,0,200))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

        self.dimmer = Dimmer(parent)

    def center(self) -> None:
        main_window = self.parent()
        dialog_rect = self.geometry()
        main_window_rect = main_window.rect()
        x = main_window_rect.x() + (main_window_rect.width() - dialog_rect.width()) / 2
        y = main_window_rect.y() + (main_window_rect.height() - dialog_rect.height()) / 2
        self.move(int(x), int(y))

        self.dimmer.setGeometry(main_window_rect)

    def open(self):
        self.center()
        self.dimmer.show()
        self.raise_()
        return super().open()

    def close(self) -> None:
        self.dimmer.close()
        self.reject()
