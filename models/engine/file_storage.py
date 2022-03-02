#!/usr/bin/python3
""" file_storage module serializes instances to a JSON file
and deserializes JSON file to instances."""

from json import dump, load
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
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects if the JSON file exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                jo = load(f)
            for k, v in jo.items():
                self.__objects[k] = eval(v["__class__"])(**v)
        except:
            pass
