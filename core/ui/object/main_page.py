# Import modules
from typing import Optional
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget
from core.style.style_manager import load_stylesheet_from_file, load_coloured_icon

# Import ui layouts
from core.ui.layout.main_page_widget import Ui_main_page_widget


class MainPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # Load ui
        self._ui = Ui_main_page_widget()
        self._ui.setupUi(self)

        # Setup ui
        self.setup_ui()

        # Style ui
        self.style_ui()

    def setup_ui(self) -> None:
        pass
    
    def style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/main_page.qss")

        # Set custom title bar icons
        close_icon_color = QColor(255, 255, 255)
        icon_size = QSize(32, 32)
        close_icon = load_coloured_icon("resources/images/icons/add.svg", close_icon_color)
        self._ui.add_button.setIconSize(icon_size)
        self._ui.add_button.setIcon(close_icon)

        maximize_icon_color = QColor(255, 255, 255)
        icon_size = QSize(24, 24)
        maximize_icon = load_coloured_icon("resources/images/icons/search.svg", maximize_icon_color)
        self._ui.search_button.setIconSize(icon_size)
        self._ui.search_button.setIcon(maximize_icon)
    
    @property
    def ui(self) -> Ui_main_page_widget:
        return self._ui
