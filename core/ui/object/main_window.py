from typing import Optional
from PySide6.QtCore import QTimer
from core.meta import get_full_version
from PySide6.QtWidgets import QWidget, QMenuBar
from qframelesswindow import FramelessMainWindow
from core.style.style_manager import load_stylesheet_from_file
import webbrowser

from core.ui.layout.main_window import Ui_main_window

from core.ui.object.title_bar import TitleBar
from core.ui.object.main_page import MainPage
from core.ui.object.generator_popup import GeneratorPopup
from core.ui.object.generator_short_popup import GeneratorShortPopup
from core.ui.object.csv_import_popup import CsvImportPopup


class MainWindow(FramelessMainWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self._title_bar = TitleBar(self)
        self.setTitleBar(self._title_bar)

        self._ui = Ui_main_window()
        self._ui.setupUi(self)

        self._main_page = MainPage(self)
        self._main_page.close()

        self._generator_popup = GeneratorPopup(self)
        self._generator_popup.close()
        
        self._generator_short_popup = GeneratorShortPopup(self)
        self._generator_short_popup.close()

        self._cvs_import_popup = CsvImportPopup(self)
        self._cvs_import_popup.close()

        self.setup_ui()
        self.style_ui()

        self.titleBar.raise_()

    def restart_service(self) -> None:
        pass

    def update_service_status(self) -> None:
        QTimer.singleShot(5000, self.update_service_status)

    def update_extension_connection(self) -> None:
        QTimer.singleShot(5000, self.update_extension_connection)

    def setup_ui(self) -> None:
        self.menuBar().hide()
        old_menu_bar = self._ui.menu_bar
        new_menu_bar = QMenuBar(self._ui.main_widget)
        for action in old_menu_bar.actions():
            new_menu_bar.addAction(action)
        self._ui.main_layout.insertWidget(0, new_menu_bar)

        title_bar_height = self.titleBar.height()
        self._ui.main_layout.setContentsMargins(0, title_bar_height, 0, 0)

        self._ui.stacked_widget.addWidget(self._main_page)

        self._ui.exit_action.triggered.connect(self.window().close)
        self._ui.create_password.triggered.connect(self._generator_popup.open)
        self._ui.create_quick_password.triggered.connect(self._generator_short_popup.open)
        self._ui.import_csv_action.triggered.connect(self._cvs_import_popup.open)
        self._ui.restart_service_action.triggered.connect(self.restart_service)
        self._ui.github_page_action.triggered.connect(lambda: webbrowser.open("https://github.com/akato-the-dragon/Obscura"))

        self.update_service_status()
        self.update_extension_connection()
        
        self._ui.action_version.setText(get_full_version())
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, "resources/styles/main_window.qss")
    
    @property
    def ui(self) -> Ui_main_window:
        return self._ui
