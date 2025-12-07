""" Module for counting program launches
"""

# Import modules
from typing import Final
from os.path import exists


# Counter file path constant
COUNTER_PATH: Final[str] = "core/runs_counter.bin"

# Counter value byte contsnts
COUNTER_VALUE_BYTES = 2
COUNTER_VALUE_SIGNED = False


def __create_counter() -> None:
    """ Creates a new counter file
    """

    # Create new counter with value 0
    with open(COUNTER_PATH, "wb") as file:
        file.write(int(0).to_bytes(COUNTER_VALUE_BYTES, signed=COUNTER_VALUE_SIGNED))


def increment_counter() -> None:
    """ Increases the counter and returns the new value
    """

    # Create new counter file if not exists
    if not exists(COUNTER_PATH):
        __create_counter()
    
    # Increment counter value
    new_value = counter_value() + 1
    
    # Write new value to file
    with open(COUNTER_PATH, "wb") as file:
        file.write(int(new_value).to_bytes(COUNTER_VALUE_BYTES, signed=COUNTER_VALUE_SIGNED))


def counter_value() -> int:
    """ Loads counter value from a binary file

    Returns:
        int: Сounter value
    """

    # Create new counter file if not exists
    if not exists(COUNTER_PATH):
        __create_counter()
    
    # Read and return counter value
    with open(COUNTER_PATH, "rb") as file:
        return int.from_bytes(file.read(), signed=COUNTER_VALUE_SIGNED)
