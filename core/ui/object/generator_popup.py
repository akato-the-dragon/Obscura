# Import modules
from PySide6.QtWidgets import   QApplication, QWidget, QLineEdit
from core.utility.password_generator import generate_password
from core.style.style_manager import load_stylesheet_from_file

# Import ui layouts
from core.ui.layout.generator_popup_widget import Ui_generator_popup_widget

# Import ui elements
from core.ui.element.popup_core import CorePopup


class GeneratorPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_generator_popup_widget()
        self._ui.setupUi(self)

        self._password_visible = False

        # Setup ui
        self.setup_ui()

        # Style ui
        self.style_ui()

    def __change_password_visiblity(self) -> None:
        self._password_visible = not self._password_visible
        
        if self._password_visible:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self._ui.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def __regenerate_password(self) -> None:
        lenght = self._ui.lenght_spin_box.value()
        use_chars = self._ui.use_chars_check_box.isChecked()
        use_upper = self._ui.use_upper_register_check_box.isChecked()
        use_symbols = self._ui.use_symbols_check_box.isChecked()

        generated_password = generate_password(lenght, use_chars, use_upper, use_symbols)
        self._ui.password_line_edit.setText(generated_password)

    def __copy_and_close(self) -> None:
        clipboard = QApplication.clipboard()
        clipboard.setText(self._ui.password_line_edit.text())
        self.__close()

    def __close(self):
        self._ui.password_line_edit.clear()
        return super().close()

    def setup_ui(self) -> None:
        self.__regenerate_password()

        self._ui.show_button.clicked.connect(self.__change_password_visiblity)
        self._ui.generate_button.clicked.connect(self.__regenerate_password)
        self._ui.copy_and_close_button.clicked.connect(self.__copy_and_close)
        self._ui.close_button.clicked.connect(self.__close)
    
    def style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/generator_popup.qss")
    
    @property
    def ui(self) -> Ui_generator_popup_widget:
        return self._ui
