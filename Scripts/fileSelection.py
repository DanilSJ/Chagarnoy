import shutil
import os


def fileSelection(path):
    try:
        shutil.move(path, f"{os.getcwd()}/processing")
    except Exception as error:
        print(error)