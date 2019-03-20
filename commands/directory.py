import os, shutil


def cd(path):
    try:
        os.chdir(path)
        print(os.getcwd())
    except FileNotFoundError:
        print("Error: Path does not exist.")


def pwd():
    print(os.getcwd())


def mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Error: File exists.")


def rmdir(path):
    try:
        os.rmdir(path)
    except OSError:
        print("Error: Directory not empty.")


def rmtree(path):
    print("WARNING: UNTESTED")
    print("WARNING: DESTRUCTIVE")
    print("WILL REMOVE DIRECTORY AND ALL CONTAINED FILES")
    print("THIS CANNOT BE UNDONE")
    cont = input("ARE YOU SURE YOU WOULD LIKE TO CONTINUE?").lower()
    if cont == 'y' or cont == 'yes':
        shutil.rmtree(path, True)
    else:
        print("Aborted")
