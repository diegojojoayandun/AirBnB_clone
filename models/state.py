#!/usr/bin/python3
"""state - module, that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State that inherits from BaseModel."""

    name = ""

    def __init__(self, *args, **kwargs):
        """User Class constructor"""

        super().__init__(self, *args, **kwargs)
