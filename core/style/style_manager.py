""" Widget styling module
"""

# Import modules
from typing import Optional
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtCore import QIODevice, QTextStream, QFile, Qt, QSize


def __set_pixmap_color(pixmap: QPixmap, color: QColor) -> QPixmap:
    """ Changes pixmap color
    Args:
        pixmap (QPixmap): Repaintable pixmap
        color (QColor): Color of the pixmap being repainted

    Returns:
        QPixmap: Repainted pixmap
    """

    # Create recolored pixmap object
    recolored_pixmap =  QPixmap(pixmap.size())
    recolored_pixmap.fill(Qt.GlobalColor.transparent)
    
    # Create recolored painter object
    painter = QPainter(recolored_pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

    # Draw original pixmap
    painter.drawPixmap(0, 0, pixmap)
    
    # Fill recolored pixmap with color
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(recolored_pixmap.rect(), color)

    painter.end()

    return recolored_pixmap


def load_stylesheet_from_string(widget: QWidget, stylesheet: str) -> None:
    """ Loads QSS style from string

    Args:
        widget (QWidget): Widget to which style is applied
        stylesheet (str): QSS style string
    """

    widget.setStyleSheet(stylesheet)


def load_stylesheet_from_file(widget: QWidget, stylesheet_path: str) -> None:
    """ Loads QSS file from file

    Args:
        widget (QWidget): Widget to which style is applied
        stylesheet_path (str): QSS style file path
    """

    # Get file stream
    stream = QFile(stylesheet_path)
    stream.open(QIODevice.OpenModeFlag.ReadOnly)

    load_stylesheet_from_string(widget, QTextStream(stream).readAll())


def load_coloured_icon(path: str, color: Optional[QColor] = None) -> QIcon:
    """ Loads icon and optionally repaints it

    Args:
        path (str): Path to the icon file
        color (Optional[QColor]): Color of the icon being repainted. Optional

    Returns:
        QIcon: Loaded or recolored (if the color is not None) icon
    """

    icon_pixmap = QPixmap(path)
    
    return QIcon(icon_pixmap if not color else __set_pixmap_color(icon_pixmap, color))


def load_coloured_pixmap(path: str, size: QSize, color: Optional[QColor] = None) -> QPixmap:
    """Loads pixmap and optionally repaints it
    Args:
        path (str): Path to the pixmap file
        size (QSize): Final pixmap size
        color (Optional[QColor]): Color of the pixmap being repainted. Optional

    Returns:
        QPixmap: Loaded or recolored (if the color is not None) pixmap
    """

    pixmap = QPixmap(path)
    recolored_pixmap = pixmap if not color else __set_pixmap_color(pixmap, color)

    return recolored_pixmap.scaled(size, Qt.TransformationMode.SmoothTransformation)
