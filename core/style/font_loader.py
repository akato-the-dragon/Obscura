from typing import Optional
from os.path import basename
from PySide6.QtCore import QDir
from PySide6.QtGui import QFontDatabase


def __get_fonts_list(directory_path: str) -> list[str]:
    folder = QDir(directory_path)
    fonts_list = []

    for entry in folder.entryList(QDir.Filter.AllEntries | QDir.Filter.NoDotAndDotDot):
        extended_prefix = f"{directory_path.rstrip('/')}/{entry}"
        
        if QDir(extended_prefix).exists():
            fonts_list.extend(__get_fonts_list(extended_prefix))

        else:
            fonts_list.append(extended_prefix)

    return fonts_list


def load_font_from_file(font_path: str) -> Optional[str]:
    font_id = QFontDatabase.addApplicationFont(font_path)

    if font_id == -1:
        return

    return basename(font_path)


def load_fonts_from_directory(directory_path: str) -> list[str]:
    loaded_fonts = []
    directory = QDir(directory_path)

    for entry in directory.entryList(QDir.Filter.AllEntries | QDir.Filter.NoDotAndDotDot):
        extended_prefix = f"{directory_path.rstrip('/')}/{entry}"
        
        if QDir(extended_prefix).exists():
            loaded_fonts.extend(load_fonts_from_directory(extended_prefix))

        else:
            loaded_font = load_font_from_file(extended_prefix)

            if loaded_font:
                loaded_fonts.append(loaded_font)

    return loaded_fonts


def get_avaible_fonts() -> list[str]:
    font_database = QFontDatabase()
    
    return font_database.families()


def is_font_avaible(font_family: str) -> bool:
    avaible_fonts = get_avaible_fonts()

    return font_family in avaible_fonts
