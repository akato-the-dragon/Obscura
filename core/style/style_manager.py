from typing import Optional
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtCore import QIODevice, QTextStream, QFile, Qt, QSize


def __set_pixmap_color(pixmap: QPixmap, color: QColor) -> QPixmap:
    recolored_pixmap =  QPixmap(pixmap.size())
    recolored_pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(recolored_pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

    painter.drawPixmap(0, 0, pixmap)

    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(recolored_pixmap.rect(), color)

    painter.end()

    return recolored_pixmap


def load_stylesheet_from_string(widget: QWidget, stylesheet: str) -> None:
    widget.setStyleSheet(stylesheet)


def load_stylesheet_from_file(widget: QWidget, stylesheet_path: str) -> None:
    stream = QFile(stylesheet_path)
    stream.open(QIODevice.OpenModeFlag.ReadOnly)

    load_stylesheet_from_string(widget, QTextStream(stream).readAll())


def load_coloured_icon(path: str, color: Optional[QColor] = None) -> QIcon:
    icon_pixmap = QPixmap(path)
    
    return QIcon(icon_pixmap if not color else __set_pixmap_color(icon_pixmap, color))


def load_coloured_pixmap(path: str, size: QSize, color: Optional[QColor] = None) -> QPixmap:
    pixmap = QPixmap(path)
    recolored_pixmap = pixmap if not color else __set_pixmap_color(pixmap, color)

    return recolored_pixmap.scaled(size, Qt.TransformationMode.SmoothTransformation)
