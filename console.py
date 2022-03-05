#!/usr/bin/python3
"""AirBnb Console - contains the entry point
of the command interpreter"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ command interpreter - using cmd class."""

    prompt = "(hbnb) "

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

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""

        line_split = line.split()
        if line == "" or line is None:
            print('** class name missing **')
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[line_split[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""

        line_split = line.split()
        if line == "" or line is None:
            print('** class name missing **')
        else:
            if line_split[0] not in classes:
                print("** class doesn't exist **")
            elif len(line_split) > 1:
                k = line_split[0] + "." + line_split[1]
                if k in models.storage.all():
                    print(models.storage.all()[k])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        and save the change into the JSON file."""

        line_split = line.split()
        if line == "" or line is None:
            print('** class name missing **')
        else:
            if line_split[0] not in classes:
                print("** class doesn't exist **")
            elif len(line_split) > 1:
                k = line_split[0] + "." + line_split[1]
                if k in models.storage.all():
                    models.storage.all().pop(k)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name."""
        line_split = line.split()
        new_dict = []
        if not line == "":
            if line_split[0] not in classes:
                print("** class doesn't exist **")
            else:
                for obj_class, obj in models.storage.all().items():
                    if type(obj).__name__ == line_split[0]:
                        new_dict.append(str(obj))
                print(new_dict)
        else:
            for obj_class, obj in models.storage.all().items():
                new_dict.append(str(obj))
            print(new_dict)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute and save the change
        into the JSON file."""

        line_split = line.split()
        if len(line_split) == 0:
            print('** class name missing **')
            return
        elif line_split[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(line_split) == 1:
            print('** instance id missing **')
            return
        else:
            k = line_split[0] + '.' + line_split[1]
            if k in models.storage.all():
                if len(line_split) > 2:
                    if len(line_split) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            models.storage.all()[k],
                            line_split[2],
                            line_split[3][1:-1])
                        models.storage.all()[k].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
