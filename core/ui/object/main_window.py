from typing import Optional
from core.meta import get_full_version
from PySide6.QtGui import QAction, QIcon
from core.service import ExtensionService
from qframelesswindow import FramelessMainWindow
from PySide6.QtCore import QThread, QTimer, QEvent
from core.utility.widget_tools import label_insert_text
from core.style.style_manager import load_stylesheet_from_file
from PySide6.QtWidgets import QApplication, QWidget, QMenuBar, QMenu, QSystemTrayIcon
import webbrowser

from core.ui.layout.main_window import Ui_main_window

from core.ui.object.title_bar import TitleBar
from core.ui.object.main_page import MainPage
from core.ui.object.generator_popup import GeneratorPopup
from core.ui.object.generator_short_popup import GeneratorShortPopup
from core.ui.object.csv_import_popup import CsvImportPopup
from core.ui.object.csv_export_popup import CsvExportPopup
from core.ui.object.set_master_popup import SetMasterPopup
from core.ui.object.remove_master_popup import RemoveMasterPopup
from core.ui.object.change_master_popup import ChangeMasterPopup


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

        self._csv_import_popup = CsvImportPopup(self)
        self._csv_import_popup.close()

        self._csv_export_popup = CsvExportPopup(self)
        self._csv_export_popup.close()

        self._change_master_popup = ChangeMasterPopup(self)
        self._change_master_popup.close()

        self._set_master_popup = SetMasterPopup(self._change_master_popup, self)
        self._set_master_popup.close()

        self._remove_master_popup = RemoveMasterPopup(self._change_master_popup, self)
        self._remove_master_popup.close()

        self._extension_service = ExtensionService()
        self._extension_thread = QThread(self)
        self.start_extension_service()

        self._tray = QSystemTrayIcon(self)

        self.setup_ui()
        self.setup_tray()
        self.style_ui()

        self.titleBar.raise_()

    def get_service_status(self) -> None:
        status = "Online" if self._extension_service.is_service_online() else "Offline"
        label_insert_text(self._ui.service_status_action, status)

        QTimer.singleShot(5000, self.get_service_status)
    
    def get_extension_status(self) -> None:
        status = self._extension_service.is_extension_online()
        self._title_bar.ui.status_widget.set_status(status)
        label_insert_text(self._ui.extension_status_action, "Online" if status else "Offline")

        QTimer.singleShot(5000, self.get_extension_status)

    def start_extension_service(self) -> None:
        self._extension_thread = QThread(self)
        self._extension_service.moveToThread(self._extension_thread)

        self._extension_thread.started.connect(self._extension_service.start_service)
        self._extension_service.server_stoped.connect(self._extension_thread.quit)
        self._extension_thread.finished.connect(self._extension_service.stop_service)

        self._extension_thread.start()

    def stop_extension_service(self) -> None:
        if self._extension_thread.isRunning():
            self._extension_thread.quit()
            if not self._extension_thread.wait(1000):
                self._extension_thread.terminate()
                self._extension_thread.wait()
        self._extension_thread.deleteLater()

    def setup_tray(self) -> None:
        self._tray.setVisible(True)
        self._tray.setIcon(QIcon("resources/images/icons/tray.png"))

        self._tray_menu = QMenu()
        self._open_app_action = QAction("Открыть")
        self._open_app_action.triggered.connect(self.show)
        self._tray_menu.addAction(self._open_app_action)

        self._close_app_action = QAction("Закрыть")
        self._close_app_action.triggered.connect(QApplication.quit)
        self._tray_menu.addAction(self._close_app_action)

        self._tray.setContextMenu(self._tray_menu)

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

        self._ui.set_master_action.triggered.connect(self._set_master_popup.open)
        self._ui.remove_master_action.triggered.connect(self._remove_master_popup.open)
        self._ui.exit_action.triggered.connect(self.window().close)
        self._ui.create_password.triggered.connect(self._generator_popup.open)
        self._ui.create_quick_password.triggered.connect(self._generator_short_popup.open)
        self._ui.import_csv_action.triggered.connect(self._csv_import_popup.open)
        self._ui.export_csv_action.triggered.connect(self._csv_export_popup.open)
        self._ui.github_page_action.triggered.connect(lambda: webbrowser.open("https://github.com/akato-the-dragon/Obscura"))
        self._ui.download_extension_action.triggered.connect(lambda: webbrowser.open("https://bormart.ru:8000/q?f=pun7bgW6VAYWNzIP"))

        label_insert_text(self._ui.action_version, get_full_version())

        self.get_service_status()
        self.get_extension_status()
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, "resources/styles/main_window.qss")
        load_stylesheet_from_file(self._tray_menu, "resources/styles/tray_menu.qss")
    
    @property
    def ui(self) -> Ui_main_window:
        return self._ui
    
    def closeEvent(self, event: QEvent) -> None:
        event.ignore()
        self.hide()
