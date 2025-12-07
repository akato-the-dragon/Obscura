# Import modules
from PySide6.QtWidgets import QWidget
from core.data_base import append_password
from core.style.style_manager import load_stylesheet_from_file

# Import ui layouts
from core.ui.layout.add_password_popup_widget import Ui_add_master_popup_widget

# Import ui elements
from core.ui.element.popup_core import CorePopup

class AddPasswordPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_add_master_popup_widget()
        self._ui.setupUi(self)

        # Setup ui
        self.setup_ui()

        # Style ui
        self.style_ui()

    def close(self):
        self._ui.site_url_line_edit.clear()
        self._ui.login_line_edit.clear()
        self._ui.password_line_edit.clear()
        return super().close()

    def add_password(self) -> None:
        site_url = self._ui.site_url_line_edit.text()
        login = self._ui.login_line_edit.text()
        password = self._ui.password_line_edit.text()
        
        append_password(site_url, login, password)
        self.parent().load_passwords_list()
        self.close()

    def setup_ui(self) -> None:
        self._ui.cancel_button.clicked.connect(self.close)
        self._ui.add_button.clicked.connect(self.add_password)
    
    def style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/add_password_popup.qss")
    
    @property
    def ui(self) -> Ui_add_master_popup_widget:
        return self._ui
