#!/usr/bin/python3
"""unnitest module"""

import datetime
import unittest
from models.review import Review

class ReviewTest(unittest.TestCase):
    """Suite of console test"""

    rw = Review()

    def test_classExist(self):
        """Test prove class exist"""

        clas = "<class 'models.review.Review'>"

        self.assertEqual(str(type(self.rw)), clas)

    def test_attributeExist(self):
        """Verify if attributtes exist"""

        self.assertTrue(hasattr(self.rw, 'place_id'))
        self.assertTrue(hasattr(self.rw, 'user_id'))
        self.assertTrue(hasattr(self.rw, 'text'))
        self.assertTrue(hasattr(self.rw, 'id'))
        self.assertTrue(hasattr(self.rw, 'created_at'))
        self.assertTrue(hasattr(self.rw, 'updated_at'))

    def test_correcttype(self):
        """Verify if the type of the attribute is correct"""

        self.assertIsInstance(self.rw.place_id, str)
        self.assertIsInstance(self.rw.user_id, str)
        self.assertIsInstance(self.rw.text, str)
        self.assertIsInstance(self.rw.id, str)
        self.assertIsInstance(self.rw.created_at, datetime.datetime)
        self.assertIsInstance(self.rw.updated_at, datetime.datetime)

    def test_inheritance(self):
        """Verify if review is subclass from BaseModel"""

        self.assertIsInstance(self.rw, Review)

if __name__ == '__main__':
    unittest.main()
