"""
This file was created as an example of working with Git branches.
"""


def delete(file: object):
    return f"{file} - files was deleted"


def create(file: object):
    return f"{file} - file was created"
    

if __name__ == '__main__':
    delete("passwords.txt")
    create(["Application", "Site", "Http"])