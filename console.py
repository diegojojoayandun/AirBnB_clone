#!/usr/bin/python3
"""AirBnb Console - contains the entry point
of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter - using cmd class"""

    prompt = "(hbnb) "  # command line prompt eq to hbnb
    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
