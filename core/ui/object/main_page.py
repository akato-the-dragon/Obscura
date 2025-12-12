from typing import Optional
from PySide6.QtGui import QIcon, Qt
from core.data_base import password_database
from PySide6.QtCore import QSize, QModelIndex
from core.style.style_manager import load_stylesheet_from_file
from PySide6.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem, QHeaderView, QMessageBox

from core.ui.layout.main_page_widget import Ui_main_page_widget

from core.ui.object.password_popup import PasswordPopup
from core.ui.object.add_password_popup import AddPasswordPopup


class MainPage(QWidget):
    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        self._ui = Ui_main_page_widget()
        self._ui.setupUi(self)

        self._add_password_popup = AddPasswordPopup(self)
        self._add_password_popup.close()

        self._password_popup = PasswordPopup(self)
        self._password_popup.close()

        self.setup_ui()
        self.style_ui()

    def load_password_data(self) -> None:
        password_list = password_database.get_password_list()
        password_filler = "?" * 32
        data = [(id, site_url, login, password_filler) for id, site_url, login in password_list]
        rows = len(data)
        columns = self._ui.table_widget.columnCount()

        self._ui.table_widget.setRowCount(rows)

        for row in range(rows):
            for column in range(columns):
                item = QTableWidgetItem(str(data[row][column]))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self._ui.table_widget.setItem(row, column, item)
            
        # Resize columns
        self._ui.table_widget.resizeColumnsToContents()

        header = self._ui.table_widget.horizontalHeader()
        header.setSectionResizeMode(self._ui.table_widget.columnCount() - 1, QHeaderView.ResizeMode.Stretch)

    def open_password_data(self, index: QModelIndex) -> None:
        selected_row = index.row()

        row_data = []
        for column in range(self._ui.table_widget.columnCount()):
            item = self._ui.table_widget.item(selected_row, column)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append("") 

        id, site_url, login, password = password_database.get_password_item(row_data[0])

        self._password_popup.open(id, site_url, login, password)

    def add_password_data(self) -> None:
        self._add_password_popup.open()

    def delete_password_data(self) -> None:
        selection_model = self._ui.table_widget.selectionModel()
        selected_rows = len(selection_model.selectedRows())

        if selected_rows > 0:
            responce = QMessageBox.question(
                self,
                "Вы уверены?",
                f"Вы действительно хотите удалить {selected_rows} записей?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

            if responce == QMessageBox.StandardButton.Yes:
                rows_to_delete = sorted([index.row() for index in selection_model.selectedRows()], reverse=True)
                for selected_row in rows_to_delete:
                    id = self._ui.table_widget.item(selected_row, 0).text()
                    password_database.remove_password(id)

    def search_password_data(self) -> None:
        target_text = self.ui.search_line_edit.text().lower()

        if not target_text:
            for row in range(self._ui.table_widget.rowCount()):
                self._ui.table_widget.setRowHidden(row, False)
            return
        for row in range(self._ui.table_widget.rowCount()):
            found = False
            for column in range(self._ui.table_widget.columnCount()):
                item = self._ui.table_widget.item(row, column)
                if item and target_text in item.text().lower():
                    found = True
                    break
            self._ui.table_widget.setRowHidden(row, not found)

    def setup_ui(self) -> None:
        self._ui.table_widget.setColumnHidden(0, True)
        self._ui.table_widget.setSortingEnabled(True)
        self._ui.table_widget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self._ui.table_widget.doubleClicked.connect(self.open_password_data)
        self._ui.add_button.clicked.connect(self.add_password_data)
        self._ui.delete_button.clicked.connect(self.delete_password_data)
        self._ui.search_button.clicked.connect(self.search_password_data)
        self._ui.search_line_edit.textChanged.connect(self.search_password_data)
        password_database.database_changed.connect(self.load_password_data)

        self.load_password_data()
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, ":/styles/main_page.qss")

        search_icon_size = QSize(24, 24)
        search_icon = QIcon(":/images/icons/search.svg")
        self._ui.search_button.setIconSize(search_icon_size)
        self._ui.search_button.setIcon(search_icon)

        delete_icon_size = QSize(32, 32)
        delete_icon = QIcon(":/images/icons/minimize.svg")
        self._ui.delete_button.setIconSize(delete_icon_size)
        self._ui.delete_button.setIcon(delete_icon)

        add_icon_size = QSize(32, 32)
        add_icon = QIcon(":/images/icons/add.svg")
        self._ui.add_button.setIconSize(add_icon_size)
        self._ui.add_button.setIcon(add_icon)
    
    @property
    def ui(self) -> Ui_main_page_widget:
        return self._ui
