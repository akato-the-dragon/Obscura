# Import modules
from core.meta import DEVELOPMENT_BUILD
from PySide6.QtWidgets import QApplication
from core.data_base import password_database
from core.utility.counter import increment_counter
from core.style.font_loader import load_fonts_from_directory
import sys

# Import ui objects
from core.ui.object.main_window import MainWindow

# Import resources
import resources.qresources.fonts


if __name__ == "__main__":
    # Create application
    application = QApplication()
    application.setStyle("Windows")

    # Increment run counter
    if DEVELOPMENT_BUILD:
        increment_counter()

    # Load fonts
    load_fonts_from_directory(":/fonts")

    # Create data base file
    password_database.create_passwords_table()

    # Create main window
    loading_window = MainWindow()
    loading_window.show()

    # Run application
    sys.exit(application.exec())

    # Close database
    password_database.close()
