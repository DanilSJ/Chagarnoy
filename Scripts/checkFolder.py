import os

def checkFolder():
    if not os.path.exists("output/"):
        os.mkdir("output/")