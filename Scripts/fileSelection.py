import shutil
import os


def fileSelection():
    path = input('Path: ')

    w = shutil.move(path, f"{os.getcwd()}/processing")
    
    if w:
        return True
    return False