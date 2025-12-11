from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from core.data_base import password_database
from PySide6.QtWidgets import QWidget, QLineEdit
from core.style.style_manager import load_stylesheet_from_file

from core.ui.layout.add_password_popup_widget import Ui_add_password_popup_widget

from core.ui.element.popup_core import CorePopup

class AddPasswordPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_add_password_popup_widget()
        self._ui.setupUi(self)

        self.setup_ui()
        self.style_ui()

    def add_password_data(self) -> None:
        site_url = self._ui.site_url_line_edit.text()
        login = self._ui.login_line_edit.text()
        password = self._ui.password_line_edit.text()

        if site_url != "" and password != "":
            password_database.add_password(site_url, login, password)
            self.cancel()
        
        else:
            self._ui.error_label.show_alert("Не заполнены необходимые поля!")

    def cancel(self) -> None:
        self._ui.site_url_line_edit.clear()
        self._ui.login_line_edit.clear()
        self._ui.password_line_edit.clear()
        self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.close()

    def show_hide_password(self) -> None:
        if self._ui.password_line_edit.echoMode() == QLineEdit.EchoMode.Password:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def setup_ui(self) -> None:
        self._ui.error_label.hide()

        self._ui.add_button.clicked.connect(self.add_password_data)
        self._ui.cancel_button.clicked.connect(self.cancel)
        self._ui.show_button.clicked.connect(self.show_hide_password)
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, ":/styles/add_password_popup.qss")

        show_icon_size = QSize(16, 16)
        show_icon = QIcon(":/images/icons/show.svg")
        self._ui.show_button.setIconSize(show_icon_size)
        self._ui.show_button.setIcon(show_icon)
    
    @property
    def ui(self) -> Ui_add_password_popup_widget:
        return self._ui
