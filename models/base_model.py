#!/usr/bin/python3
"""base model class module"""


from uuid import uuid4
from datetime import datetime
from models import storage

time_format = "%Y-%m-%dT%H:%M:%S.%f"  # string object in ISO format


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs) -> None:
        """class constructor"""
        if kwargs is not None and kwargs != {}:  # validar si hay params (dict)
            for key, value in kwargs.items():
                # cada clave del dict es un atributo de instancia existente
                if key == 'created_at' or key == 'updated at':
                    value = datetime.strptime(value, time_format)
                # se crean claves/atributos de instancia exepto para __class__
                if key != '__class__':
                    setattr(self, key, value)
        else:  # si no hay argumentos es una nueva instancia
            self.id = str(uuid4())  # public instance attribute
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representation of an instance."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        custom_dict = self.__dict__.copy()
        custom_dict['__class__'] = type(self).__name__
        custom_dict['created_at'] = custom_dict['created_at'].isoformat()
        custom_dict['updated_at'] = custom_dict['updated_at'].isoformat()
        return custom_dict
