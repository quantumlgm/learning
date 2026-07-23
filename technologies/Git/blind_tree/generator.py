"""
A simple CLI tool to generate secure random passwords.
"""

import random
import string


def generate_password(length: int =16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


if __name__ == "__main__":
    print(generate_password())