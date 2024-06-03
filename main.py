from Scripts.checkFolder import checkFolder
from Scripts.fileSelection import fileSelection
from Scripts.chagarnoy import chagarnoy


if __name__ == '__main__':
    checkFolder()
    text = fileSelection('D:/Chagarnoy/README.md')
    print(chagarnoy(text))