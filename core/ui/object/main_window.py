# Import modules
from typing import Optional
from core.meta import get_full_version
from PySide6.QtWidgets import QWidget, QMenuBar
from qframelesswindow import FramelessMainWindow
from core.style.style_manager import load_stylesheet_from_file
import webbrowser

# Import ui layouts
from core.ui.layout.main_window import Ui_main_window

# Import ui objects
from core.ui.object.title_bar import TitleBar
from core.ui.object.main_page import MainPage
from core.ui.object.about_page import AboutPage


class MainWindow(FramelessMainWindow):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # Load titlebar
        self._title_bar = TitleBar(self)
        self.setTitleBar(self._title_bar)

        # Load ui
        self._ui = Ui_main_window()
        self._ui.setupUi(self)

        # Setup ui
        self.setup_ui()

        # Style ui
        self.style_ui()

        # Raise title bar
        self.titleBar.raise_()

    def __open_page(self, index: int) -> None:
        self._ui.stacked_widget.setCurrentIndex(index)

    def setup_ui(self) -> None:
        # Move menu bar
        self.menuBar().hide()
        old_menu_bar = self._ui.menu_bar
        new_menu_bar = QMenuBar(self._ui.main_widget)
        for action in old_menu_bar.actions():
            new_menu_bar.addAction(action)
        self._ui.main_layout.insertWidget(0, new_menu_bar)

        title_bar_height = self.titleBar.height()
        self._ui.main_layout.setContentsMargins(0, title_bar_height, 0, 0)

        # Set action version
        self._ui.action_version.setText(get_full_version())

        # Add main page
        self._main_page = MainPage()
        self._ui.stacked_widget.addWidget(self._main_page)

        # Add about page
        self._about_page = AboutPage()
        self._ui.stacked_widget.addWidget(self._about_page)

        # Connect actions
        self._ui.general_action.triggered.connect(lambda: self.__open_page(0))
        self._ui.exit_action.triggered.connect(lambda: self.window().close())
        
        self._ui.about_action.triggered.connect(lambda: self.__open_page(1))
        self._ui.github_page_action.triggered.connect(lambda: webbrowser.open("https://github.com/akato-the-dragon/Obscura"))
    
    def style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/main_window.qss")
    
    @property
    def ui(self) -> Ui_main_window:
        return self._ui
