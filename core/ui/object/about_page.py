# Import modules
from typing import Optional
from PySide6.QtWidgets import QWidget

# Import ui layouts
from core.ui.layout.about_page_widget import Ui_about_page_widget


class AboutPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # Load ui
        self._ui = Ui_about_page_widget()
        self._ui.setupUi(self)

        # Setup ui
        self.setup_ui()

        # Style ui
        self.style_ui()

    def setup_ui(self) -> None:
        pass
    
    def style_ui(self) -> None:
        pass
    
    @property
    def ui(self) -> Ui_about_page_widget:
        return self._ui
