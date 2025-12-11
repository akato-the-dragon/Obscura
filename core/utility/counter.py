from typing import Final
from os.path import exists
from core.utility.resource_path import get_resource_path


COUNTER_PATH: Final[str] = get_resource_path("core/runs_counter.bin")

COUNTER_VALUE_BYTES = 2
COUNTER_VALUE_SIGNED = False


def __create_counter() -> None:
    with open(COUNTER_PATH, "wb") as file:
        file.write(int(0).to_bytes(COUNTER_VALUE_BYTES, signed=COUNTER_VALUE_SIGNED))


def increment_counter() -> None:
    if not exists(COUNTER_PATH):
        __create_counter()
    
    new_value = counter_value() + 1
    
    with open(COUNTER_PATH, "wb") as file:
        file.write(int(new_value).to_bytes(COUNTER_VALUE_BYTES, signed=COUNTER_VALUE_SIGNED))


def counter_value() -> int:
    if not exists(COUNTER_PATH):
        __create_counter()

    with open(COUNTER_PATH, "rb") as file:
        return int.from_bytes(file.read(), signed=COUNTER_VALUE_SIGNED)
    
