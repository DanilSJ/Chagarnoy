import shutil
from readFile import readFile
import os


def fileSelection(path):
    try:
        readFile(path)
    except Exception as error:
        print(error)