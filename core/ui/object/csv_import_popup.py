from core.data_base import password_database
from core.style.style_manager import load_stylesheet_from_file
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal, QObject
import csv

from core.ui.layout.csv_import_popup_widget import Ui_csv_import_popup_widget
from core.ui.element.popup_core import CorePopup


class CSVImportWorker(QObject):
    progress = Signal(int)
    finished = Signal(int)
    error = Signal(str)
    
    def __init__(self, file_path, mapped_columns):
        super().__init__()
        self.file_path = file_path
        self.mapped_columns = mapped_columns
        self._is_running = True
    
    def run(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader, [])
                
                if not headers:
                    self.error.emit("Файл не содержит заголовков.")
                    return
                
                total_lines = sum(1 for _ in file)
                file.seek(0)
                next(reader)
                
                counter = 0
                processed = 0
                
                for row in reader:
                    if not self._is_running:
                        break
                        
                    if len(row) < len(headers):
                        processed += 1
                        continue
                    
                    row_dict = {}
                    for field, col_name in self.mapped_columns.items():
                        col_index = headers.index(col_name) if col_name in headers else -1
                        if col_index >= 0 and col_index < len(row):
                            row_dict[field] = row[col_index].strip()
                        else:
                            row_dict[field] = ""
                    
                    site_url = row_dict.get("site_url")
                    login = row_dict.get("login")
                    password = row_dict.get("password")
                    
                    # Добавление в базу данных
                    password_database.add_password(site_url, login, password)
                    counter += 1
                    processed += 1
                    
                    # Отправка прогресса
                    progress_percent = int((processed / total_lines) * 100) if total_lines > 0 else 0
                    self.progress.emit(progress_percent)
            
            if self._is_running:
                self.finished.emit(counter)
                
        except Exception as e:
            if self._is_running:
                self.error.emit(f"Не удалось импортировать файл:\n{str(e)}")
    
    def stop(self):
        """Остановка импорта"""
        self._is_running = False


class CsvImportPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_csv_import_popup_widget()
        self._ui.setupUi(self)

        self._current_file_path = ""
        self._column_headers = []
        self._mapped_columns = {}
        
        # Для управления потоками
        self._import_thread = None
        self._import_worker = None

        self.setup_ui()
        self.style_ui()

    def open(self) -> None:
        super().open()

    def cancel(self) -> None:
        if self._import_worker:
            self._import_worker.stop()
            self._import_thread.quit()
            self._import_thread.wait()
        
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
        
        self.set_ui_enabled(False)
        
        self._ui.progress_bar.setRange(0, 100)
        self._ui.progress_bar.setValue(0)

        self._import_thread = QThread()
        self._import_worker = CSVImportWorker(self._current_file_path, self._mapped_columns)

        self._import_worker.moveToThread(self._import_thread)

        self._import_thread.started.connect(self._import_worker.run)
        self._import_worker.progress.connect(self.update_progress)
        self._import_worker.finished.connect(self.on_import_finished)
        self._import_worker.error.connect(self.on_import_error)
        self._import_thread.finished.connect(self.cleanup_thread)

        self._import_thread.start()

    def update_progress(self, value: int):
        self._ui.progress_bar.setValue(value)

    def on_import_finished(self, count: int):
        QMessageBox.information(self, "Успех", f"Импортировано {count} записей.")
        self.cleanup_thread()
        self.set_ui_enabled(True)
        self.close()

    def on_import_error(self, error_message: str):
        QMessageBox.critical(self, "Ошибка", error_message)
        self.cleanup_thread()
        self.set_ui_enabled(True)

    def cleanup_thread(self):
        if self._import_thread:
            self._import_thread.quit()
            self._import_thread.wait()
            self._import_thread = None
            self._import_worker = None

    def set_ui_enabled(self, enabled: bool):
        self._ui.csv_file_browser_button.setEnabled(enabled)
        self._ui.import_button.setEnabled(enabled)
        self._ui.cancel_button.setEnabled(enabled)
        self._ui.site_url_combo_box.setEnabled(enabled)
        self._ui.login_combo_box.setEnabled(enabled)
        self._ui.password_combo_box.setEnabled(enabled)

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
                
                self._column_headers = headers

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

    def closeEvent(self, event):
        self.cancel()
        super().closeEvent(event)
