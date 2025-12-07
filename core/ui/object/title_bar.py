# Import modules
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget
from qframelesswindow import TitleBarBase
from core.meta import get_full_version, NAME
from qframelesswindow.utils import toggleMaxState
from core.utility.widget_tools import label_insert_text
from core.style.style_manager import load_stylesheet_from_file, load_coloured_icon

# Import ui layouts
from core.ui.layout.title_bar_widget import Ui_title_bar_widget


class TitleBar(TitleBarBase):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        # Load ui
        self._ui = Ui_title_bar_widget()
        self._ui.setupUi(self)

        # Setup ui
        self.setup_ui()

        # Style ui
        self.style_ui()

    def setup_ui(self) -> None:
        # Hide base title bar buttons
        self.closeBtn.hide()
        self.maxBtn.hide()
        self.minBtn.hide()

        # Connect base slots to custom buttons
        self._ui.close_button.clicked.connect(self.window().close)
        self._ui.maximize_button.clicked.connect(lambda: toggleMaxState(self.window()))
        self._ui.minimize_button.clicked.connect(self.window().showMinimized)

        # Set version text
        label_insert_text(self._ui.version_label, get_full_version(), ".")

        # Set app name text
        self._ui.name_label.setText(NAME)

    def style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/title_bar.qss")

        # Set custom title bar icons
        icon_size = QSize(24, 24)

        close_icon_color = QColor(255, 255, 255)
        close_icon = load_coloured_icon("resources/images/icons/close.svg", close_icon_color)
        self._ui.close_button.setIconSize(icon_size)
        self._ui.close_button.setIcon(close_icon)

        maximize_icon_color = QColor(255, 255, 255)
        maximize_icon = load_coloured_icon("resources/images/icons/maximize.svg", maximize_icon_color)
        self._ui.maximize_button.setIconSize(icon_size)
        self._ui.maximize_button.setIcon(maximize_icon)

        minimize_icon_color = QColor(255, 255, 255)
        minimize_icon = load_coloured_icon("resources/images/icons/minimize.svg", minimize_icon_color)
        self._ui.minimize_button.setIconSize(icon_size)
        self._ui.minimize_button.setIcon(minimize_icon)

    @property
    def ui(self) -> Ui_title_bar_widget:
        return self._ui
