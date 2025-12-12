from core.meta import NAME, DEVELOPMENT_BUILD
from PySide6.QtWidgets import QApplication
from core.data_base import password_database
from core.utility.counter import increment_counter
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from core.style.font_loader import load_fonts_from_directory
import os
import sys
import psutil

from core.ui.object.main_window import MainWindow

import resources.qresources.fonts
import resources.qresources.styles
import resources.qresources.images


if __name__ == "__main__":
    socket = QLocalSocket()
    socket.connectToServer(NAME)
    if socket.waitForConnected(100):
        sys.exit(1)

    server = QLocalServer()
    server.listen(NAME)

    application = QApplication()
    application.setStyle("Windows")

    if DEVELOPMENT_BUILD:
        increment_counter()

    load_fonts_from_directory(":/fonts")

    password_database.create_passwords_table()

    loading_window = MainWindow()
    loading_window.show()

    sys.exit(application.exec())

    password_database.close()
