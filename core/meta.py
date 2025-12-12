from typing import Final
from core.utility.counter import counter_value

COMPANY: Final[str] = "AkaDevProductions"
NAME: Final[str] = "Obscura"
VERSION: Final[str] = "1.0.0"
AUTHOR: Final[str] = "akato-the-dragon"
LICENSE: Final[str] = "MIT"
DEVELOPMENT_BUILD: Final[bool] = True


def get_meta() -> dict:
    return {
        "company": COMPANY,
        "name": NAME,
        "version": VERSION,
        "full_version": get_full_version(),
        "author": AUTHOR,
        "license": LICENSE,
        "development_build": DEVELOPMENT_BUILD
    }


def get_full_version() -> str:
    return f"{VERSION}.{counter_value()}"
