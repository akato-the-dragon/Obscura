from core.meta import NAME
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from core.meta import get_full_version
from qframelesswindow import TitleBarBase
from qframelesswindow.utils import toggleMaxState
from core.style.style_manager import load_stylesheet_from_file

from core.ui.layout.title_bar_widget import Ui_title_bar_widget


class TitleBar(TitleBarBase):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self._ui = Ui_title_bar_widget()
        self._ui.setupUi(self)

        self.setup_ui()
        self.style_ui()

    def __insert_version(self) -> None:
        label = self._ui.version_label
        text, _ = label.text().split(".")

        label.setText(f"{text}. {get_full_version()}")

    def setup_ui(self) -> None:
        self.closeBtn.hide()
        self.maxBtn.hide()
        self.minBtn.hide()

        self._ui.close_button.clicked.connect(self.window().close)
        self._ui.maximize_button.clicked.connect(lambda: toggleMaxState(self.window()))
        self._ui.minimize_button.clicked.connect(self.window().showMinimized)

        self._ui.name_label.setText(NAME)

        self.__insert_version()

    def style_ui(self) -> None:
        load_stylesheet_from_file(self, ":/styles/title_bar.qss")

        close_icon_size = QSize(24, 24)
        close_icon = QIcon(":/images/icons/close.svg")
        self._ui.close_button.setIconSize(close_icon_size)
        self._ui.close_button.setIcon(close_icon)

        maximize_icon_size = QSize(24, 24)
        maximize_icon = QIcon(":/images/icons/maximize.svg")
        self._ui.maximize_button.setIconSize(maximize_icon_size)
        self._ui.maximize_button.setIcon(maximize_icon)

        minimize_icon_size = QSize(24, 24)
        minimize_icon = QIcon(":/images/icons/minimize.svg")
        self._ui.minimize_button.setIconSize(minimize_icon_size)
        self._ui.minimize_button.setIcon(minimize_icon)

    @property
    def ui(self) -> Ui_title_bar_widget:
        return self._ui
