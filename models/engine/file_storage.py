#!/usr/bin/python3
"""file_storage module that serializes instances to a JSON file
and deserializes JSON file to instances.
Arguments: None
"""

from json import dump, load
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel,
           "User": User, "State": State,
           "City": City,
           "Amenity": Amenity,
           "Place": Place,
           "Review": Review
           }


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects.
        Arguments: None"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id."""

        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the
        JSON file (path: __file_path)."""

        json_obj = {}
        for k in self.__objects:
            json_obj[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as f:
            dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects if the JSON file exists
        otherwise, do nothing. If file doesn’t exist, no exception raised."""

        if not path.exists(FileStorage.__file_path):
            return
        with open(self.__file_path, 'r', encoding='utf-8') as f:
            j = load(f)
            for k in j:
                self.__objects[k] = classes[j[k]['__class__']](**j[k])
