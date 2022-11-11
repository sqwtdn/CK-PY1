from random import choice
from string import ascii_letters, digits


def get_random_password() -> str:
    n = 8
    pass_chars = ascii_letters + digits
    password = ''.join(choice(pass_chars) for _ in range(n))
    return password


print(get_random_password())
