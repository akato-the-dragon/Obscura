from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from core.password_generator import generate_password
from PySide6.QtWidgets import QWidget, QLineEdit, QApplication
from core.style.style_manager import load_stylesheet_from_file

from core.ui.layout.generator_popup_widget import Ui_generator_popup_widget

from core.ui.element.popup_core import CorePopup


class GeneratorPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_generator_popup_widget()
        self._ui.setupUi(self)

        self.setup_ui()
        self.style_ui()

    def open(self) -> None:
        self.generate_password()
        super().open()

    def cancel(self) -> None:
        self._ui.lenght_spin_box.setValue(8)
        self._ui.use_chars_check_box.setChecked(False)
        self._ui.use_upper_register_check_box.setChecked(False)
        self._ui.use_symbols_check_box.setChecked(False)
        self._ui.password_line_edit.clear()
        self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        super().close()

    def copy_password(self) -> None:
        clipboard = QApplication.clipboard()
        clipboard.setText(self._ui.password_line_edit.text())
        self.cancel()

    def generate_password(self) -> None:
        lenght = self._ui.lenght_spin_box.value()
        use_chars = self._ui.use_chars_check_box.isChecked()
        use_upper = self._ui.use_upper_register_check_box.isChecked()
        use_symbols = self._ui.use_symbols_check_box.isChecked()

        generated_password = generate_password(lenght, use_chars, use_upper, use_symbols)
        self._ui.password_line_edit.setText(generated_password)

    def show_hide_password(self) -> None:
        if self._ui.password_line_edit.echoMode() == QLineEdit.EchoMode.Password:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def setup_ui(self) -> None:
        self._ui.show_button.clicked.connect(self.show_hide_password)
        self._ui.generate_button.clicked.connect(self.generate_password)
        self._ui.copy_button.clicked.connect(self.copy_password)
        self._ui.close_button.clicked.connect(self.cancel)
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, "resources/styles/generator_popup.qss")

        show_icon_size = QSize(16, 16)
        show_icon = QIcon("resources/images/icons/show.svg")
        self._ui.show_button.setIconSize(show_icon_size)
        self._ui.show_button.setIcon(show_icon)

        generate_icon_size = QSize(16, 16)
        generate_icon = QIcon("resources/images/icons/retry.svg")
        self._ui.generate_button.setIconSize(generate_icon_size)
        self._ui.generate_button.setIcon(generate_icon)
    
    @property
    def ui(self) -> Ui_generator_popup_widget:
        return self._ui
