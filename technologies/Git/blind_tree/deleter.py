"""
This file was created as an example of working with Git branches.
"""


from typing import Callable


def delete(file: object):
    return f"{file} - files was deleted"


def create(file: object):
    return f"{file} - file was created"


def generate_deleter(func: Callable[object, str]):
    print("Process is starting")
    yield func
    print("Process is completed")

if __name__ == '__main__':
    delete("passwords.txt")
    create(["Application", "Site", "Http"])
     
    for s in generate_deleter(delete("main.py")):
        print(s)