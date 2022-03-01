#!/usr/bin/python3
"""to create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
storage = FileStorage()  # create variable storage as instance file_storage
storage.reload()  # call reload() method on this variable
