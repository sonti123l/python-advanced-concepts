from contextlib import contextmanager
import os


@contextmanager
def change_directory_and_manage_directory(destination):
    current_directory = os.getcwd()
    os.chdir(destination)
    try:
        yield "\n"
    finally:
        os.chdir(current_directory)
        print("changed to current working directory again",os.getcwd())

with change_directory_and_manage_directory("/tmp"):
    print("changed directory to temporary directory",os.getcwd())



