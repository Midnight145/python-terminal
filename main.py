import importlib
import sys, os
import commands.coreutils

class Command:
    def __init__(self, com):
        self.command = com
        self.arguments = [i for i in self.command.split(" ")]
        self.base = self.arguments[0]

    def parser(self):
        pass


command_names = {}
for filename in os.listdir("commands"):
    command_names[filename] = os.path.splitext(filename)[0]
print(command_names)

print("PyTerm 0.1")
print("Currently in", sys.path[0])

command = Command(input(">>> "))
while command.base != "exit":
    try:
        command_ = getattr(commands.coreutils, command.base) # coreutils system
        print(command_(command.arguments))

    except AttributeError:
        for key, value in command_names.items():
            if command.base == value:
                thing = importlib.import_module("commands", package=key)
                command_ = getattr(getattr(thing, value), value)
                print(command_(command.arguments))
    command = Command(input(">>> "))