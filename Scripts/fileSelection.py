import shutil
import os


path = input('Path: ')

shutil.move(path, f"{os.getcwd()}/processing")