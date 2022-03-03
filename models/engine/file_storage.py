#!/usr/bin/python3
""" file_storage module serializes instances to a JSON file
and deserializes JSON file to instances."""

from json import dump, load
from models.base_model import BaseModel
from models.user import User


classes = {"BaseModel": BaseModel, "user": User}


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""

        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)."""

        json_obj = {}
        for k in self.__objects:
            json_obj[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as f:
            dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects if the JSON file exists
        otherwise, do nothing. If file doesn’t exist, no exception raised."""

        from os import path

        if not path.exists(FileStorage.__file_path):
            return
        with open(self.__file_path, 'r', encoding='utf-8') as f:
            json_obj = load(f)
            for k in json_obj:
                self.__objects[k] = classes[json_obj[k][
                                    '__class__']](**json_obj[k])
