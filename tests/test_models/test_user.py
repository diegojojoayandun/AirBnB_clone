#!/usr/bin/python3
"""unnitest module"""

import unittest
from models.user import User
import datetime


class UserTest(unittest.TestCase):
    """Suite of console test"""

    us = User()

    def test_ClassExist(self):
        """Test prove class exist"""

        clas = "<class 'models.user.User'>"

        self.assertEqual(str(type(self.us)), clas)

    def test_atributesExist(self):
        """Verify if attributtes exist"""

        self.assertTrue(hasattr(self.us, 'email'))
        self.assertTrue(hasattr(self.us, 'password'))
        self.assertTrue(hasattr(self.us, 'first_name'))
        self.assertTrue(hasattr(self.us, 'last_name'))
        self.assertTrue(hasattr(self.us, 'id'))
        self.assertTrue(hasattr(self.us, 'created_at'))
        self.assertTrue(hasattr(self.us, 'updated_at'))

    def test_correctType(self):
        """Verify if the type of the attribute is correct"""

        self.assertIsInstance(self.us.email, str)
        self.assertIsInstance(self.us.password, str)
        self.assertIsInstance(self.us.first_name, str)
        self.assertIsInstance(self.us.last_name, str)
        self.assertIsInstance(self.us.id, str)
        self.assertIsInstance(self.us.created_at, datetime.datetime)
        self.assertIsInstance(self.us.updated_at, datetime.datetime)

    def test_inheritance(self):
        """Verify if user is subclass from BaseModel"""

        self.assertIsInstance(self.us, User)


if __name__ == '__main__':
    unittest.main()
