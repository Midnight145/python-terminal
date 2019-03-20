import os


def touch(path):
    try:
        open(path, 'w').close()
        os.lchmod(path, 0o644)
    except FileExistsError:
        print("Error: File {} already exists".format(path))
        return 1


def chmod(args):
    # os.chmod expects the mode to be in base 8 so we have to convert it here.
    os.lchmod(args[0], int(args[1], 8))


def edit(path):
    with open(path, 'w') as file:
        pass


def mv(src, dest):
    os.rename(src, dest)


def rename(src, dest):
    if touch(dest) == 1:
        ovw = input("File {} already exists! Overwrite?")
        if ovw == 'y' or ovw == 'yes':
            mv(src, dest)
        else:
            print("Abourted")
    else:
        mv(src, dest)