#!/usr/bin/python3
"""review - module, that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review that inherits from BaseModel."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """User Class constructor"""

        super().__init__(self, *args, **kwargs)
