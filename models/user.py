#!/usr/bin/python3
"""users - module, that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User Class constructor"""

        super().__init__(self, *args, **kwargs)
