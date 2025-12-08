# Import modules
from typing import Optional, List, Dict
from PySide6.QtWidgets import (
    QWizard, QWizardPage, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFileDialog, QTableWidget, QTableWidgetItem, QComboBox, QMessageBox,
    QLineEdit, QGroupBox, QTextEdit
)
from PySide6.QtCore import Qt
from core.data_base import append_password, get_passwords_list, get_password_item
from core.utility.password_encrypt import encrypt
import csv


class CsvImportWizard(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Мастер импорта паролей")
        self.resize(800, 600)

        # Data
        self.csv_data: List[List[str]] = []
        self.headers: List[str] = []
        self.column_mapping: Dict[str, str] = {}

        self.setPage(PageIntro.Id, PageIntro(self))
        self.setPage(PageFileSelect.Id, PageFileSelect(self))
        self.setPage(PagePreview.Id, PagePreview(self))
        self.setPage(PageMapping.Id, PageMapping(self))
        self.setPage(PageImport.Id, PageImport(self))

        self.db_fields = ["site_url", "login", "password", "description"]

    def get_csv_headers(self) -> List[str]:
        return self.headers

    def get_csv_data(self) -> List[List[str]]:
        return self.csv_data

    def set_csv_data(self, headers: List[str], data: List[List[str]]):
        self.headers = headers
        self.csv_data = data

    def set_column_mapping(self, mapping: Dict[str, str]):
        self.column_mapping = mapping

    def get_column_mapping(self) -> Dict[str, str]:
        return self.column_mapping


# --- Страница 1: Введение ---
class PageIntro(QWizardPage):
    Id = 1

    def __init__(self, wizard: CsvImportWizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Импорт паролей из CSV")
        label = QLabel(
            "Этот мастер поможет импортировать пароли из CSV-файла "
            "(например, из браузера, LastPass или Bitwarden).\n\n"
            "Поддерживаются файлы с колонками: URL, Логин, Пароль, Описание."
        )
        label.setWordWrap(True)
        layout = QVBoxLayout(self)
        layout.addWidget(label)


# --- Страница 2: Выбор файла ---
class PageFileSelect(QWizardPage):
    Id = 2

    def __init__(self, wizard: CsvImportWizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Выбор CSV-файла")

        self.file_path_edit = QLineEdit()
        self.file_path_edit.setReadOnly(True)
        browse_button = QPushButton("Обзор...")
        browse_button.clicked.connect(self._browse_file)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Путь к CSV-файлу:"))
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.file_path_edit)
        hlayout.addWidget(browse_button)
        layout.addLayout(hlayout)

        self._sample_preview = QTextEdit()
        self._sample_preview.setReadOnly(True)
        self._sample_preview.setMaximumHeight(100)
        layout.addWidget(QLabel("Пример содержимого:"))
        layout.addWidget(self._sample_preview)

    def _browse_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выберите CSV-файл", "", "CSV Files (*.csv);;All Files (*)"
        )
        if path:
            self.file_path_edit.setText(path)
            self._load_sample(path)

    def _load_sample(self, path: str):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                sample = f.read(500)  # первые 500 символов
            self._sample_preview.setPlainText(sample)
        except Exception as e:
            self._sample_preview.setPlainText(f"Ошибка: {str(e)}")

    def validatePage(self) -> bool:
        path = self.file_path_edit.text()
        if not path:
            QMessageBox.warning(self, "Ошибка", "Выберите CSV-файл.")
            return False

        # Загружаем полный CSV
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
                if not rows:
                    raise ValueError("Файл пуст")
                self.wizard.set_csv_data(rows[0], rows[1:])  # первая строка — заголовки
            return True
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось прочитать CSV:\n{str(e)}")
            return False


# --- Страница 3: Предпросмотр ---
class PagePreview(QWizardPage):
    Id = 3

    def __init__(self, wizard: CsvImportWizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Предварительный просмотр")

        self.table = QTableWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Данные из CSV-файла (первые 10 строк):"))
        layout.addWidget(self.table)

    def initializePage(self):
        headers = self.wizard.get_csv_headers()
        data = self.wizard.get_csv_data()[:10]  # только первые 10 строк

        self.table.clear()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

        for row_idx, row in enumerate(data):
            for col_idx, cell in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(cell))

        self.table.resizeColumnsToContents()


# --- Страница 4: Сопоставление колонок ---
class PageMapping(QWizardPage):
    Id = 4

    def __init__(self, wizard: CsvImportWizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Сопоставление полей")
        self.setSubTitle("Сопоставьте колонки CSV с полями базы данных.")

        self.mapping_widgets: Dict[str, QComboBox] = {}
        layout = QVBoxLayout(self)

        group = QGroupBox("Сопоставление:")
        group_layout = QVBoxLayout(group)
        layout.addWidget(group)

        headers = ["site_url", "login", "password", "description"]
        labels = ["URL сайта", "Логин", "Пароль", "Описание"]

        for db_field, label in zip(headers, labels):
            hlayout = QHBoxLayout()
            hlayout.addWidget(QLabel(f"{label}:"))
            combo = QComboBox()
            combo.setObjectName(db_field)
            self.mapping_widgets[db_field] = combo
            hlayout.addWidget(combo)
            group_layout.addLayout(hlayout)

        # Обязательные поля
        self.registerField("site_url*", self.mapping_widgets["site_url"])
        self.registerField("login*", self.mapping_widgets["login"])
        self.registerField("password*", self.mapping_widgets["password"])

    def initializePage(self):
        headers = self.wizard.get_csv_headers()
        for db_field, combo in self.mapping_widgets.items():
            combo.clear()
            combo.addItems(headers)
            # Попытка авто-сопоставления
            guess = self._guess_column(db_field, headers)
            if guess:
                combo.setCurrentText(guess)

    def _guess_column(self, db_field: str, headers: List[str]) -> Optional[str]:
        """Пытается угадать колонку по названию"""
        aliases = {
            "site_url": ["url", "сайт", "адрес", "website", "site"],
            "login": ["логин", "username", "user", "email", "login", "имя"],
            "password": ["пароль", "password", "pass"],
            "description": ["описание", "notes", "примечание", "comment", "description"]
        }
        for header in headers:
            h_lower = header.lower()
            for alias in aliases.get(db_field, []):
                if alias in h_lower:
                    return header
        return headers[0] if headers else None

    def validatePage(self) -> bool:
        mapping = {}
        used_headers = set()
        for db_field, combo in self.mapping_widgets.items():
            header = combo.currentText()
            if not header:
                QMessageBox.warning(self, "Ошибка", f"Выберите колонку для '{db_field}'")
                return False
            if header in used_headers:
                QMessageBox.warning(self, "Ошибка", f"Колонка '{header}' использована дважды!")
                return False
            used_headers.add(header)
            mapping[db_field] = header
        self.wizard.set_column_mapping(mapping)
        return True


# --- Страница 5: Импорт ---
class PageImport(QWizardPage):
    Id = 5

    def __init__(self, wizard: CsvImportWizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Импорт данных")
        self.setFinalPage(True)

        self.status_label = QLabel("Готово к импорту.")
        self.import_button = QPushButton("Импортировать")
        self.import_button.clicked.connect(self._do_import)

        layout = QVBoxLayout(self)
        layout.addWidget(self.status_label)
        layout.addWidget(self.import_button, alignment=Qt.AlignCenter)

    def initializePage(self):
        self.import_button.setEnabled(True)
        self.status_label.setText("Нажмите 'Импортировать', чтобы начать.")

    def _do_import(self):
        try:
            mapping = self.wizard.get_column_mapping()
            csv_headers = self.wizard.get_csv_headers()
            csv_data = self.wizard.get_csv_data()

            # Индексы колонок
            col_indices = {
                db_field: csv_headers.index(csv_col)
                for db_field, csv_col in mapping.items()
            }

            success_count = 0
            error_lines = []

            for i, row in enumerate(csv_data, start=2):  # строка 1 — заголовки
                if len(row) <= max(col_indices.values()):
                    error_lines.append(i)
                    continue

                try:
                    site_url = row[col_indices["site_url"]].strip()
                    login = row[col_indices["login"]].strip()
                    raw_password = row[col_indices["password"]].strip()
                    description = row[col_indices["description"]].strip() if "description" in col_indices else ""

                    if not site_url or not login or not raw_password:
                        error_lines.append(i)
                        continue

                    encrypted_password = encrypt(raw_password)
                    append_password(site_url, login, encrypted_password, description)
                    success_count += 1

                except Exception as e:
                    print(f"Ошибка в строке {i}: {e}")
                    error_lines.append(i)

            # Отчёт
            msg = f"Импорт завершён!\nУспешно: {success_count} записей."
            if error_lines:
                msg += f"\nОшибки в строках: {', '.join(map(str, error_lines[:5]))}"
                if len(error_lines) > 5:
                    msg += f" и ещё {len(error_lines) - 5}"

            self.status_label.setText(msg)
            self.import_button.setEnabled(False)

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось импортировать:\n{str(e)}")


def export_passwords_to_csv(parent=None):
    """
    Экспортирует все пароли из базы в CSV-файл.
    Пароли расшифровываются перед записью.
    """
    # 1. Получаем все записи (без паролей)
    try:
        password_list = get_passwords_list()  # [(id, site_url, login, description), ...]
        if not password_list:
            QMessageBox.information(parent, "Экспорт", "Нет записей для экспорта.")
            return
    except Exception as e:
        QMessageBox.critical(parent, "Ошибка", f"Не удалось прочитать базу:\n{str(e)}")
        return

    # 2. Выбираем путь для сохранения
    default_filename = "exported_passwords.csv"
    path, _ = QFileDialog.getSaveFileName(
        parent,
        "Сохранить как CSV",
        default_filename,
        "CSV Files (*.csv);;All Files (*)"
    )
    if not path:
        return  # отмена

    # 3. Добавляем расширение .csv, если нужно
    if not path.lower().endswith('.csv'):
        path += '.csv'

    # 4. Записываем CSV
    try:
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

            # Заголовки
            writer.writerow(["site_url", "login", "password", "description, notes"])

            # Данные
            for item in password_list:
                item_id, site_url, login, description = item
                try:
                    # Получаем полную запись с расшифрованным паролем
                    full_item = get_password_item(item_id)
                    _, _, _, decrypted_password, full_description = full_item

                    writer.writerow([
                        site_url or "",
                        login or "",
                        decrypted_password or "",
                        full_description or description or ""
                    ])
                except Exception as e:
                    print(f"Пропущена запись ID={item_id}: {e}")
                    # Пропускаем проблемную запись, но продолжаем
                    writer.writerow([site_url or "", login or "", "[ОШИБКА ДЕШИФРОВКИ]", description or ""])

        # 5. Успешное завершение
        QMessageBox.information(
            parent,
            "Экспорт завершён",
            f"Экспортировано {len(password_list)} записей.\nФайл сохранён:\n{path}"
        )

    except PermissionError:
        QMessageBox.critical(
            parent,
            "Ошибка доступа",
            f"Нет прав на запись в файл:\n{path}\n\nПопробуйте выбрать другую папку."
        )
    except Exception as e:
        QMessageBox.critical(
            parent,
            "Ошибка экспорта",
            f"Не удалось сохранить CSV:\n{str(e)}"
        )