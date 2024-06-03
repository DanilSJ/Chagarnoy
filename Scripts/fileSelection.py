from .readFile import readFile

def fileSelection(path):
    try:
        readFile(path)
    except Exception as error:
        print(error)