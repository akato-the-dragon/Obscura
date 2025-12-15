from typing import Optional, List, Tuple
from core.data_base import password_database
from PySide6.QtCore import QThread, Signal, QObject
from core.style.style_manager import load_stylesheet_from_file
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
import os
import csv

from core.ui.layout.csv_export_popup_widget import Ui_csv_export_popup_widget

from core.ui.element.popup_core import CorePopup


class CsvExportWorker(QObject):
    progress = Signal(int)
    finished = Signal(int)
    error = Signal(str)
    
    def __init__(self, file_path: str, headers: List = ["site_url", "login", "password"],
                 parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.file_path = file_path
        self._headers = headers
        self._is_running = True
        
    def run(self):
        try:
            total_lines = len(password_database.get_password_list())
            processed = 0
            
            with open(self.file_path, "w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(self._headers)
                
                for password_item in password_database.get_password_list():
                    item_id = password_item[0]
                    
                    id, site_url, login, password = password_database.get_password_item(item_id)

                    writer.writerow((site_url, login, password))
                    processed += 1

                    progress_percent = int((processed / total_lines) * 100) if total_lines > 0 else 0
                    self.progress.emit(progress_percent)
            
            if self._is_running:
                self.finished.emit(processed)
            
        except Exception as e:
            if self._is_running:
                self.error.emit(f"Не удалось экспортировать файл:\n{str(e)}")

    def stop(self):
        self._is_running = False


class CsvExportPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_csv_export_popup_widget()
        self._ui.setupUi(self)

        self._current_file_path = ""

        self._export_thread = None
        self._export_worker = None

        self.setup_ui()
        self.style_ui()

    def open(self):
        self._ui.csv_file_line_edit.clear()
        self._ui.progress_bar.setValue(0)
        super().open()

    def cancel(self) -> None:
        if self._export_worker:
            self._export_worker.stop()
            self._export_thread.quit()
            self._export_thread.wait()
        
        super().close()

    def export_csv_data(self) -> None:
        if not self._current_file_path:
            QMessageBox.warning(self, "Ошибка", "Не выбран файл для импорта.")
            return

        headers = ["site_url", "login", "password"]
        
        self.set_ui_enabled(False)

        self._export_thread = QThread()
        self._export_worker = CsvExportWorker(self._current_file_path, headers)

        self._export_worker.moveToThread(self._export_thread)

        self._export_thread.started.connect(self._export_worker.run)
        self._export_worker.progress.connect(self.update_progress)
        self._export_worker.finished.connect(self.on_export_finished)
        self._export_worker.error.connect(self.on_export_error)
        self._export_thread.finished.connect(self.cleanup_thread)

        self._export_thread.start()

    def update_progress(self, value: int):
        self._ui.progress_bar.setValue(value)

    def on_export_finished(self, count: int):
        QMessageBox.information(self, "Успех", f"Экспортировано {count} записей.")
        self.cleanup_thread()
        self.set_ui_enabled(True)
        self.close()

    def on_export_error(self, error_message: str):
        QMessageBox.critical(self, "Ошибка", error_message)
        self.cleanup_thread()
        self.set_ui_enabled(True)

    def cleanup_thread(self):
        if self._export_thread:
            self._export_thread.quit()
            self._export_thread.wait()
            self._export_thread = None
            self._export_worker = None

    def set_ui_enabled(self, enabled: bool):
        self._ui.csv_file_browser_button.setEnabled(enabled)
        self._ui.export_button.setEnabled(enabled)
        self._ui.cancel_button.setEnabled(enabled)

    def get_csv_file(self) -> None:
        """Открыть диалог выбора файла"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить CSV файл",
            os.path.expanduser("~") + "/passwords.csv",
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if file_path:
            self._current_file_path = file_path
            self.ui.csv_file_line_edit.setText(file_path)

    def setup_ui(self) -> None:
        self._ui.csv_file_browser_button.clicked.connect(self.get_csv_file)
        self._ui.export_button.clicked.connect(self.export_csv_data)
        self._ui.cancel_button.clicked.connect(self.cancel)
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, ":/styles/csv_export_popup.qss")
    
    @property
    def ui(self) -> Ui_csv_export_popup_widget:
        return self._ui

    def closeEvent(self, event):
        self.cancel()
        super().closeEvent(event)
