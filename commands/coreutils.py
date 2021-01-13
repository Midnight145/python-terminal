import os
import shutil


def cd(path, *trash):
    try:
        os.chdir(path[1])
        return os.getcwd()
    except FileNotFoundError:
        print("Error: Path does not exist.")
        return 1


def pwd(*trash):
    return os.getcwd()


def mkdir(path):
    try:
        os.mkdir(path)
        return path
    except FileExistsError:
        print("Error: File exists.")
        return 1


def rmdir(path):
    try:
        os.rmdir(path)
        return 0
    except OSError:
        print("Error: Directory not empty.")
        return 1


def rmtree(path):
    print("WARNING: UNTESTED")
    print("WARNING: DESTRUCTIVE")
    print("WILL REMOVE DIRECTORY AND ALL CONTAINED FILES")
    print("THIS CANNOT BE UNDONE")
    cont = input("ARE YOU SURE YOU WOULD LIKE TO CONTINUE?").lower()
    if cont == 'y' or cont == 'yes':
        shutil.rmtree(path, True)
        return 0
    else:
        print("Aborted")
        return 1


def touch(path):
    try:
        open(path, 'w').close()
        os.lchmod(path, 0o644)
        return 0
    except FileExistsError:
        print("Error: File {} already exists".format(path))
        return 1


def chmod(args):
    # os.chmod expects the mode to be in base 8 so we have to convert it here.
    try:
        os.lchmod(args[0], int(args[1], 8))
        return 0
    except:
        return 1


def mv(src, dest):
    try:
        os.rename(src, dest)
        return 0
    except:
        return 1


def rename(src, dest):
    if touch(dest) == 1:
        ovw = input("File {} already exists! Overwrite?")
        if ovw == 'y' or ovw == 'yes':
            mv(src, dest)
        else:
            print("Aborted")
            return 1
    else:
        mv(src, dest)
        return 0
