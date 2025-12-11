from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from core.data_base import password_database
from PySide6.QtWidgets import QWidget, QLineEdit
from core.password_encrypt import encrypt, decrypt
from core.style.style_manager import load_stylesheet_from_file

from core.ui.layout.remove_master_popup_widget import Ui_remove_master_popup_widget

from core.ui.object.change_master_popup import ChangeMasterPopup

from core.ui.element.popup_core import CorePopup

class RemoveMasterPopup(CorePopup):
    def __init__(self, change_master_popup: ChangeMasterPopup, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_remove_master_popup_widget()
        self._ui.setupUi(self)

        self._change_master_popup = change_master_popup

        self._master_path = "data/master"     

        self.setup_ui()
        self.style_ui()

    def remove_password(self) -> None:
        with open(self._master_path, "w+") as file:
            old_master = "" if file.read() == "" else decrypt(file.read(), "")

            current_master = self._ui.password_line_edit.text()

            if current_master == old_master:
                new_master = ""
                encrypted_master = encrypt(new_master, "")
                file.write(encrypted_master)

                self._change_master_popup.change_master(new_master, old_master)

                password_database.set_master_password(new_master)

    def show_hide_password(self) -> None:
        if self._ui.password_line_edit.echoMode() == QLineEdit.EchoMode.Password:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def cancel(self) -> None:
        self._ui.password_line_edit.clear()
        self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.close()

    def setup_ui(self) -> None:
        self._ui.remove_button.clicked.connect(self.remove_password)
        self._ui.cancel_button.clicked.connect(self.cancel)
        self._ui.show_button.clicked.connect(self.show_hide_password)

        self._ui.error_label.hide()
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, "resources/styles/remove_master_popup.qss")

        show_icon_size = QSize(16, 16)
        show_icon = QIcon("resources/images/icons/show.svg")
        self._ui.show_button.setIconSize(show_icon_size)
        self._ui.show_button.setIcon(show_icon)
    
    @property
    def ui(self) -> Ui_remove_master_popup_widget:
        return self._ui
