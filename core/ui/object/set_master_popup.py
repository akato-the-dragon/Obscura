from PySide6.QtWidgets import QWidget
from core.style.style_manager import load_stylesheet_from_file

from core.ui.layout.set_master_popup_widget import Ui_set_master_popup_widget

from core.ui.element.popup_core import CorePopup

class SetMasterPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_set_master_popup_widget()
        self._ui.setupUi(self)

        self.setup_ui()
        self.style_ui()

    def setup_ui(self) -> None:
        pass
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, "resources/styles/set_master_popup.qss")
    
    @property
    def ui(self) -> Ui_set_master_popup_widget:
        return self._ui
