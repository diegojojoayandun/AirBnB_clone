#!/usr/bin/python3
"""base model class module"""


from uuid import uuid4
from datetime import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """class constructor."""

        if kwargs:
            for (k, v) in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, time_format)
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime."""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
