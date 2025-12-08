from core.data_base import password_database
from core.style.style_manager import load_stylesheet_from_file
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
import csv

from core.ui.layout.csv_import_popup_widget import Ui_csv_import_popup_widget

from core.ui.element.popup_core import CorePopup


class CsvImportPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_csv_import_popup_widget()
        self._ui.setupUi(self)

        self._current_file_path = ""
        self._column_headers = []
        self._mapped_columns = {}

        self.setup_ui()
        self.style_ui()

    def open(self) -> None:
        super().open()

    def cancel(self) -> None:
        super().close()

    def import_csv_data(self) -> None:
        if not self._current_file_path:
            QMessageBox.warning(self, "Ошибка", "Не выбран файл для импорта.")
            return

        required_fields = ["site_url", "login", "password"]
        for field in required_fields:
            if not self._mapped_columns.get(field):
                QMessageBox.warning(self, "Ошибка", f"Не сопоставлено поле: {field}")
                return

        try:
            with open(self._current_file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader, [])

                counter = 0
                for row in reader:
                    if len(row) < len(headers):
                        continue
                    
                    row_dict = {}
                    for field, col_name in self._mapped_columns.items():
                        col_index = headers.index(col_name) if col_name in headers else -1
                        if col_index >= 0 and col_index < len(row):
                            row_dict[field] = row[col_index].strip()
                        else:
                            row_dict[field] = ""
                    
                    site_url = row_dict.get("site_url")
                    login = row_dict.get("login")
                    password = row_dict.get("password")
                    password_database.add_password(site_url, login, password)
                    counter += 1
            
            QMessageBox.information(self, "Успех", f"Импортировано {counter} записей.")
            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось импортировать файл:\n{str(e)}")

    def get_csv_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите CSV файл",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if file_path:
            self._current_file_path = file_path
            self._ui.csv_file_line_edit.setText(file_path)
            self.load_csv_headers(file_path)

    def load_csv_headers(self, file_path: str) -> None:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader, [])
                
                if not headers:
                    QMessageBox.warning(self, "Предупреждение", "Файл не содержит заголовков.")
                    return
                
                self.column_headers = headers

                for combo in [self._ui.site_url_combo_box, self._ui.login_combo_box, self._ui.password_combo_box]:
                    combo.clear()
                    combo.addItem("-- Не выбрано --")
                    for header in headers:
                        combo.addItem(header)
                
                self._mapped_columns.clear()
                
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось прочитать файл:\n{str(e)}")

    def update_mapping(self, field: str) -> None:
        combo = getattr(self._ui, f"{field}_combo_box")
        selected_text = combo.currentText()
        
        if selected_text == "-- Не выбрано --":
            self._mapped_columns.pop(field, None)
        else:
            self._mapped_columns[field] = selected_text

    def setup_ui(self) -> None:
        self._ui.csv_file_browser_button.clicked.connect(self.get_csv_file)
        self._ui.import_button.clicked.connect(self.import_csv_data)
        self._ui.cancel_button.clicked.connect(self.cancel)

        self._ui.site_url_combo_box.currentIndexChanged.connect(lambda: self.update_mapping("site_url"))
        self._ui.login_combo_box.currentIndexChanged.connect(lambda: self.update_mapping("login"))
        self._ui.password_combo_box.currentIndexChanged.connect(lambda: self.update_mapping("password"))
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, "resources/styles/csv_import_popup.qss")
    
    @property
    def ui(self) -> Ui_csv_import_popup_widget:
        return self._ui
