"""
This file was created as an example of working with Git branches.
"""


from typing import Callable


class FilePanel:
    @staticmethod    
    def delete(file: object):
        return f"{file} - files was deleted"


    @staticmethod
    def create(file: object):
        return f"{file} - file was created"


    @staticmethod
    def generate_deleter(func: Callable[object, str]):
        print("Process is starting")
        yield func
        print("Process is completed")


if __name__ == '__main__':
    fp = FilePanel()
    fp.delete("passwords.txt")
    fp.create(["Application", "Site", "Http"])
     
    for s in fp.generate_deleter(fp.delete("main.py")):
        print(s)