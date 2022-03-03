#!/usr/bin/python3
"""city - module, that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """User Class constructor"""

        super().__init__(self, *args, **kwargs)
