#!/usr/bin/python3
""" file_storage module serializes instances to a JSON file
and deserializes JSON file to instances."""

from json import dump, load
from os import path
from models.base_model import BaseModel

class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects if the JSON file exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        if (path.isfile(self.__file_path)):
            with open(self.__file_path, 'r', encoding="utf-8") as fname:
                l_json = load(fname)
                for k, v in l_json.items():
                    self.__objects[k] = eval(
                        v['__class__'])(**v)
