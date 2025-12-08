# Import modules
from core.utility.password_encrypt import encrypt, decrypt
import sqlite3

# Create connection
connection = sqlite3.connect("passwords.db", autocommit=True)


def create_passwords_table() -> None:
    cursor = connection.cursor()
    query = """CREATE TABLE IF NOT EXISTS password (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_url TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    description TEXT);"""
    cursor.execute(query)


def get_passwords_list() -> list[tuple]:
    cursor = connection.cursor()
    query = """SELECT id, site_url, login, description FROM password"""
    return cursor.execute(query).fetchall()


def get_password_item(id: int) -> tuple:
    cursor = connection.cursor()
    query = """SELECT id, site_url, login, password, description FROM password WHERE id=?"""
    password_item = cursor.execute(query, (id,)).fetchall()[0]
    decrypted_password = decrypt(password_item[3])
    return (password_item[0], password_item[1], password_item[2],
            decrypted_password, password_item[4])


def append_password(site_url: str, login: str, password: str, description: str = "") -> None:
    encrypted_password = encrypt(password)
    cursor = connection.cursor()
    query = """INSERT INTO password (site_url, login, password, description) VALUES(?, ?, ?, ?)"""
    cursor.execute(query, (site_url, login, encrypted_password, description))


def remove_password(id: int) -> None:
    cursor = connection.cursor()
    query = """DELETE FROM password WHERE id=?"""
    cursor.execute(query, (id,))
