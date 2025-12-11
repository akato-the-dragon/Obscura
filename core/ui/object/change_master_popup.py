from typing import Optional
from core.data_base import password_database
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QThread, Signal, QObject
from core.style.style_manager import load_stylesheet_from_file

from core.ui.layout.change_master_popup_widget import Ui_change_master_popup_widget

from core.ui.element.popup_core import CorePopup


class ChangeMasterWorker(QObject):
    progress = Signal(int)
    finished = Signal(int)
    error = Signal(str)
    
    def __init__(self, new_master: str, old_master: str, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self._new_master = new_master
        self._old_master = old_master
        self._is_running = True
        
    def run(self):
        try:
            password_ids = [item[0] for item in password_database.get_password_list()]
            total_lines = len(password_ids)
            processed = 0

            for password_id in password_ids:
                password_item = password_database.get_password_item(password_id, self._old_master)
                id, site_url, login, password = password_item

                password_database.remove_password(password_id)
                password_database.add_password(site_url, login, password, self._new_master)

                processed += 1

                progress_percent = int((processed / total_lines) * 100) if total_lines > 0 else 0
                self.progress.emit(progress_percent)
            
            if self._is_running:
                self.finished.emit(processed)

        except Exception as e:
            if self._is_running:
                self.error.emit(f"Не удалось Обновить пароль:\n{str(e)}")

    def stop(self):
        self._is_running = False


class ChangeMasterPopup(CorePopup):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        
        self._ui = Ui_change_master_popup_widget()
        self._ui.setupUi(self)

        self._change_master_worker = None
        self._change_master_thread = None

        self.setup_ui()
        self.style_ui()

    def change_master(self, new_master: str, old_master: str) -> None:
        self.open()

        self._change_master_thread = QThread(self)
        self._change_master_worker = ChangeMasterWorker(new_master, old_master)

        self._change_master_worker.moveToThread(self._change_master_thread)

        self._change_master_thread.started.connect(self._change_master_worker.run)
        self._change_master_worker.progress.connect(self.update_progress)
        self._change_master_worker.finished.connect(self.on_master_change_finished)
        self._change_master_worker.error.connect(self.on_master_change_error)
        self._change_master_thread.finished.connect(self.cleanup_thread)

        self._change_master_thread.start()

    def cleanup_thread(self):
        if self._export_thread:
            self._export_thread.quit()
            self._export_thread.wait()
            self._export_thread = None
            self._export_worker = None

    def update_progress(self, value: int):
        self._ui.progress_bar.setValue(value)

    def on_master_change_error(self, error_message: str):
            QMessageBox.critical(self, "Ошибка", error_message)
            self.cleanup_thread()
            self.close()

    def on_master_change_finished(self, count: int):
        QMessageBox.information(self, "Успех", "Пароли были обновлены.")
        self.cleanup_thread()
        self.close()

    def setup_ui(self) -> None:
        pass
    
    def style_ui(self) -> None:
        load_stylesheet_from_file(self, "resources/styles/change_master_popup.qss")
    
    @property
    def ui(self) -> Ui_change_master_popup_widget:
        return self._ui
