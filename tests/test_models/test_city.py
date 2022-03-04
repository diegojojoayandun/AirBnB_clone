#!/usr/bin/python3
"""unnitest module"""

import unittest
from models.city import City
import datetime


class CityTest(unittest.TestCase):
    """Suite of console test"""

    cy = City()

    def test_classExist(self):
        """prove if class exist"""

        exist = "<class 'models.city.City'>"

        self.assertEqual(str(type(self.cy)), exist)

    def test_attributeExist(self):
        """prove if attribute exist"""

        self.assertTrue(hasattr(self.cy, 'name'))
        self.assertTrue(hasattr(self.cy, 'id'))
        self.assertTrue(hasattr(self.cy, 'created_at'))
        self.assertTrue(hasattr(self.cy, 'updated_at'))
        self.assertTrue(hasattr(self.cy, 'state_id'))

    def test_correctType(self):
        """Verify if the type of the attribute is correct"""

        self.assertIsInstance(self.cy.id, str)
        self.assertIsInstance(self.cy.name, str)
        self.assertIsInstance(self.cy.created_at, datetime.datetime)
        self.assertIsInstance(self.cy.updated_at, datetime.datetime)
        self.assertIsInstance(self.cy.state_id, str)

    def test_inheritance(self):
        """prove if city inherits from BaseModel"""

        self.assertTrue(self.cy, City)

if __name__ == '__main__':
    unittest.main()
