#!/usr/bin/python3
""" file_storage module serializes instances to a JSON file
and deserializes JSON file to instances."""


from json import dump, loads
from os import path


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"  # string - path to the JSON file
    __objects = {}  # dictionary - empty but will store objs by <class name>.id

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

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

        if not path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
            content_file = f.read()  # In this case, return string of dict.
            obj_Json = loads(content_file)  # Result = dict

            for key in obj_Json:
                dict_value = obj_Json[key]
                name_class = dict_value["__class__"]
                new_obj = eval(name_class)(**dict_value)
                FileStorage.__objects[key] = new_obj
