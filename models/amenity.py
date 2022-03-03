#!/usr/bin/python3
"""amenity - module, that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel."""

    name = ""

    def __init__(self, *args, **kwargs):
        """User Class constructor"""

        super().__init__(self, *args, **kwargs)
