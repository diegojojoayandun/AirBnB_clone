#!/usr/bin/python3
"""AirBnb Console - contains the entry point
of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter - using cmd class"""

    prompt = "(hbnb) "  # command line prompt eq to hbnb
    pass

    def do_EOF(self, line):
        """Ctrl + D command, Exit the program."""
        print()
        return True

    def do_quit(self, line):
        """Quit Command to Exit the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on an empty line + ENTER."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
