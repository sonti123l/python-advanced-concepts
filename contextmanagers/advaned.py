import os

class contextmanager:
    def __init__(self,file_method):
        self.file_method = file_method

    def __enter__(self):
        self.file_method()

    def __exit__(self,exctype,excvalue):
        if self.file_method():
            return True
        self.file_method.close()


def change_directory_and_manage_directory(destination):
    current_directory = os.getcwd()
    os.chdir(destination)
    try:
        yield "\n"
    finally:
        os.chdir(current_directory)
        return "changed to current working directory again",os.getcwd()

with contextmanager(change_directory_and_manage_directory("/tmp")):
    print("changed directory to temporary directory",os.getcwd())



