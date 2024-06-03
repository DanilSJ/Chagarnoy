from .readFile import readFile

def fileSelection(path):
    try:
        return readFile(path)
    except Exception as error:
        return print(error)