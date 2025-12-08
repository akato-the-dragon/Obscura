# Import modules
from typing import Optional
from PySide6.QtGui import QColor
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHeaderView
from core.data_base import get_passwords_list, remove_password
from PySide6.QtWidgets import QTableWidgetItem, QAbstractItemView
from core.style.style_manager import load_stylesheet_from_file, load_coloured_icon

# Import ui layouts
from core.ui.layout.main_page_widget import Ui_main_page_widget

# Import ui objects
from core.ui.object.confirm_popup import ConfirmPopup
from core.ui.object.add_password_popup import AddPasswordPopup


class MainPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # Load ui
        self._ui = Ui_main_page_widget()
        self._ui.setupUi(self)

        self._add_password_popup = AddPasswordPopup(self)
        self._add_password_popup.close()

        self._confirm_popup = ConfirmPopup(self, self.delete_passwords)
        self._confirm_popup.close()

        # Setup ui
        self.setup_ui()

        # Style ui
        self.style_ui()

    def load_passwords_list(self) -> None:
        password_filler = "?" * 32
        data = [(id, site_url, login, password_filler) for id, site_url, login, description in get_passwords_list()]
        rows = len(data)
        columns = self._ui.passwords_table_widget.columnCount()

        self._ui.passwords_table_widget.setRowCount(rows)

        for row in range(rows):
            for column in range(columns):
                item = QTableWidgetItem(str(data[row][column]))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self._ui.passwords_table_widget.setItem(row, column, item)
            
        # Resize columns
        self._ui.passwords_table_widget.resizeColumnsToContents()

        header = self._ui.passwords_table_widget.horizontalHeader()
        header.setSectionResizeMode(self._ui.passwords_table_widget.columnCount() - 1, QHeaderView.ResizeMode.Stretch)

    def delete_passwords(self) -> None:
        table = self._ui.passwords_table_widget
        selection_model = table.selectionModel()
        
        for selected_row in selection_model.selectedRows(0):
            id = table.item(selected_row.row(), 0).text()
            remove_password(id)
            self.load_passwords_list()

    def confirm_delete_passowrds(self) -> None:
        counter = len(self._ui.passwords_table_widget.selectionModel().selectedRows())

        if counter > 0:
            self._confirm_popup.open()

    def search_passwords(self) -> None:
        table = self._ui.passwords_table_widget
        target_text = self.ui.search_line_edit.text().lower()

        if not target_text:
            for row in range(table.rowCount()):
                table.setRowHidden(row, False)
            return
        for row in range(table.rowCount()):
            found = False
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item and target_text in item.text().lower():
                    found = True
                    break
            table.setRowHidden(row, not found)
     
    def setup_ui(self) -> None:
        self._ui.passwords_table_widget.setColumnHidden(0, True)
        self._ui.passwords_table_widget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # Load passwords list
        self.load_passwords_list()

        self._ui.add_button.clicked.connect(self._add_password_popup.open)
        self._ui.search_button.clicked.connect(self.search_passwords)
        self._ui.delete_button.clicked.connect(self.confirm_delete_passowrds)
    
    def style_ui(self) -> None:
        # Set stylesheet
        load_stylesheet_from_file(self, "resources/styles/main_page.qss")

        # Set custom title bar icons
        close_icon_color = QColor(255, 255, 255)
        icon_size = QSize(32, 32)
        close_icon = load_coloured_icon("resources/images/icons/add.svg", close_icon_color)
        self._ui.add_button.setIconSize(icon_size)
        self._ui.add_button.setIcon(close_icon)

        search_icon_color = QColor(255, 255, 255)
        search_icon_size = QSize(24, 24)
        search_icon = load_coloured_icon("resources/images/icons/search.svg", search_icon_color)
        self._ui.search_button.setIconSize(search_icon_size)
        self._ui.search_button.setIcon(search_icon)

        delete_icon_color = QColor(255, 255, 255)
        delete_icon_size = QSize(24, 24)
        delete_icon = load_coloured_icon("resources/images/icons/minimize.svg", delete_icon_color)
        self._ui.delete_button.setIconSize(delete_icon_size)
        self._ui.delete_button.setIcon(delete_icon)
    
    @property
    def ui(self) -> Ui_main_page_widget:
        return self._ui
