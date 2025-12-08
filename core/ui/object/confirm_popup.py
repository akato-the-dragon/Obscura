# Import modules
from PySide6.QtWidgets import QWidget
from core.style.style_manager import load_stylesheet_from_file

# Import ui layouts
from core.ui.layout.confirm_popup_widget import Ui_confirm_popup_widget

# Import ui elements
from core.ui.element.popup_core import CorePopup


class ConfirmPopup(CorePopup):
    def __init__(self, parent: QWidget, continue_func) -> None:
        super().__init__(parent)
        
        self._ui = Ui_confirm_popup_widget()
        self._ui.setupUi(self)

        # Setup ui
        self.setup_ui(continue_func)

        # Style ui
        self.style_ui()

    def setup_ui(self, continue_func) -> None:
        self._ui.continue_button.clicked.connect(continue_func)
        self._ui.continue_button.clicked.connect(self.close)
        self._ui.cancel_button.clicked.connect(self.close)
    
    def style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/confirm_popup.qss")
    
    @property
    def ui(self) -> Ui_confirm_popup_widget:
        return self._ui
