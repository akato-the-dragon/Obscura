import random


def generate_password(lenght: int = 8, use_chars = True, use_upper = True, use_symbols: bool = True) -> str:
    numbers = list("0123456789")
    chars = list("qwertyuiopasdfghjklzxcvbnm")
    chars_upper = list(map(str.upper, chars))
    symbols = list("!@#$%^&*()_+-=[]{}|;:,.<>?")

    password_list = numbers

    if use_chars:
        password_list += chars
    if use_upper:
        password_list += chars_upper
    if use_symbols:
        password_list += symbols
    
    random.shuffle(password_list)

    return "".join([random.choice(password_list) for x in range(lenght)])
