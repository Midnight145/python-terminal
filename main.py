import sys, os
from commands.directory import cd, pwd
from commands.file import touch, chmod


class Command:
    def __init__(self, com):
        self.command = com
        self.arguments = [i for i in self.command.split(" ")]
        self.base = self.arguments[0]

    def parser(self):
        pass


print("PyTerm 0.1")
print("Currently in", sys.path[0])

command = Command(input(">>> "))
if command.base == "pwd":
    print("here")
    pwd()
if command.base == "cd":
    print("here")
    cd(command.arguments[1])
    pwd()
if command.base == "touch":
    touch(command.arguments[1])
if command.base == "chmod":
    chmod(command.arguments[1::])