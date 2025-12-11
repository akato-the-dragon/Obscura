from typing import Optional
from PySide6.QtCore import QObject, Signal
from core.password_encrypt import encrypt, decrypt
import sqlite3


class PasswordDatabase(QObject):
    database_changed = Signal()

    def __init__(self, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)
        self._connection = sqlite3.connect("passwords.db", autocommit=True, check_same_thread=False)

    def create_passwords_table(self) -> None:
        cursor = self._connection.cursor()
        query = """CREATE TABLE IF NOT EXISTS password (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site_url TEXT NOT NULL,
        login TEXT NOT NULL,
        password TEXT NOT NULL);
        """
        cursor.execute(query)

    def get_password_list(self) -> list[tuple]:
        cursor = self._connection.cursor()
        query = """SELECT id, site_url, login FROM password"""
        return cursor.execute(query).fetchall()

    def get_password_item(self, id: int) -> tuple:
        cursor = self._connection.cursor()
        query = """SELECT id, site_url, login, password FROM password WHERE id = ?"""
        password_item = cursor.execute(query, (id,)).fetchall()[0]
        decrypted_password = decrypt(password_item[3], "")
        return (password_item[0], password_item[1], password_item[2],
                decrypted_password)

    def update_password(self, id: int, site_url: str, login: str, password: str) -> None:
        encrypted_password = encrypt(password)
        cursor = self._connection.cursor()
        query = """UPDATE password
        SET
        site_url = ?,
        login = ?, 
        password =?

        WHERE id = ?
        """
        cursor.execute(query, (site_url, login, encrypted_password, id))
        self.database_changed.emit()

    def add_password(self, site_url: str, login: str, password: str) -> None:
        encrypted_password = encrypt(password, "")
        cursor = self._connection.cursor()
        query = """INSERT INTO password (site_url, login, password) VALUES(?, ?, ?)"""
        cursor.execute(query, (site_url, login, encrypted_password))
        self.database_changed.emit()

    def remove_password(self, id: int) -> None:
        cursor = self._connection.cursor()
        query = """DELETE FROM password WHERE id=?"""
        cursor.execute(query, (id,))
        self.database_changed.emit()

    def close(self) -> None:
        self._connection.close()


password_database = PasswordDatabase()
