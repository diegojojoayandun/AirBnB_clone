#!/usr/bin/python3
"""unnitest module"""

import unittest
from models.place import Place
import datetime

class PlaceTest(unittest.TestCase):
    """Suite of console test"""

    pl = Place()

    def test_ClassExist(self):
        """verify class exist"""

        clp = "<class 'models.place.Place'>"

        self.assertTrue(str(type(self.pl)), clp)

    def test_attributeExist(self):
        """verify attributes exist"""

        self.assertTrue(hasattr(self.pl, 'city_id'))
        self.assertTrue(hasattr(self.pl, 'user_id'))
        self.assertTrue(hasattr(self.pl, 'name'))
        self.assertTrue(hasattr(self.pl, 'description'))
        self.assertTrue(hasattr(self.pl, 'number_rooms'))
        self.assertTrue(hasattr(self.pl, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pl, 'max_guest'))
        self.assertTrue(hasattr(self.pl, 'price_by_night'))
        self.assertTrue(hasattr(self.pl, 'latitude'))
        self.assertTrue(hasattr(self.pl, 'longitude'))
        self.assertTrue(hasattr(self.pl, 'amenity_ids'))
        self.assertTrue(hasattr(self.pl, 'id'))
        self.assertTrue(hasattr(self.pl, 'created_at'))
        self.assertTrue(hasattr(self.pl, 'updated_at'))

    def test_correctType(self):
        """Verify if the type of the attribute is correct"""

        self.assertIsInstance(self.pl.city_id, str)
        self.assertIsInstance(self.pl.user_id, str)
        self.assertIsInstance(self.pl.name, str)
        self.assertIsInstance(self.pl.description, str)
        self.assertIsInstance(self.pl.number_rooms, int)
        self.assertIsInstance(self.pl.number_bathrooms, int)
        self.assertIsInstance(self.pl.max_guest, int)
        self.assertIsInstance(self.pl.price_by_night, int)
        self.assertIsInstance(self.pl.latitude, float)
        self.assertIsInstance(self.pl.longitude, float)
        self.assertIsInstance(self.pl.amenity_ids, list)
        self.assertIsInstance(self.pl.id, str)
        self.assertIsInstance(self.pl.created_at, datetime.datetime)
        self.assertIsInstance(self.pl.updated_at, datetime.datetime)

    def test_inheritance(self):
        """Verify if amenity is subclass from BaseModel"""

        self.assertIsInstance(self.pl, Place)

if __name__ == '__main__':
    unittest.main()
