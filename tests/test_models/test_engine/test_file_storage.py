#!/usr/bin/python3
"""Unittest for FileStorage"""

import unittest
import os
import pycodestyle
import models
from models.engine.file_storage import FileStorage
from models.engine import file_storage
from models.base_model import BaseModel


FileStorage = file_storage.FileStorage


class Test_FileStorage(unittest.TestCase):
    """unitest - Test FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """set up before every test method"""
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """Remove test instances"""
        del cls.storage
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_check_if_hasattr(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(models.storage, "_FileStorage__file_path"))
        self.assertTrue(type(self.storage._FileStorage__file_path) is str)

    def test_pep8_test_style(self):
        """Pep8 style test"""
        pep8_codstyle = pycodestyle.StyleGuide(quiet=True)
        res = pep8_codstyle.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "State class needs a docstring")

    def test_all(self):
        """Test method All"""
        s_dict = self.storage.all()
        self.assertIsInstance(s_dict, dict)
        self.assertIs(s_dict, self.storage._FileStorage__objects)

    def test_new(self):
        """test method new"""
        s_dict = self.storage.all()
        bas = BaseModel()
        kk = "{}.{}".format(type(bas).__name__, bas.id)
        self.assertTrue(kk in s_dict.keys())

    def test_save(self):
        """test method save"""
        self.assertIsNotNone(FileStorage.save)
        self.storage.save()
        with open("file.json", 'r') as reader:
            string = reader.readlines()

        try:
            os.remove("file.json")
        except BaseException:
            pass

        self.storage.save()

        with open("file.json", 'r') as reader:
            string2 = reader.readlines()

        self.assertEqual(string, string2)
        self.assertTrue(os.path.exists("file.json"))

    def help_test_save(self, classname):
        """Helps tests save() method for classname."""
        self.resetStorage()
        cls = storage.classes()[classname]
        o = cls()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {key: o.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_5_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.help_test_save("BaseModel")

    def test_5_save_user(self):
        """Tests save() method for User."""
        self.help_test_save("User")

    def test_5_save_state(self):
        """Tests save() method for State."""
        self.help_test_save("State")

    def test_5_save_city(self):
        """Tests save() method for City."""
        self.help_test_save("City")

    def test_5_save_amenity(self):
        """Tests save() method for Amenity."""
        self.help_test_save("Amenity")

    def test_5_save_place(self):
        """Tests save() method for Place."""
        self.help_test_save("Place")

    def test_5_save_review(self):
        """Tests save() method for Review."""
        self.help_test_save("Review")

    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_reload(self):
        """test method reload"""
        self.assertIsNotNone(FileStorage.reload)
        try:
            os.remove("file.json")
        except BaseException:
            pass
        with open("file.json", "w") as writer:
            writer.write("{}")
        with open("file.json", "r") as reader:
            for l in reader:
                self.assertEqual(l, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
