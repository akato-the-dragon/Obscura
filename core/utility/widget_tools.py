# Import modules
from typing import Any
from PySide6.QtWidgets import QLabel


def label_insert_text(label: QLabel, value: Any, separator: str = ":") -> None:
    if label.text().find(separator) > 0:
        text, _ = label.text().split(separator)
        label.setText(f"{text}{separator} {value}")
    else:
        label.setText(value)
