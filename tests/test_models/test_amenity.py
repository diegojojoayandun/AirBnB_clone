#!/usr/bin/python3
"""unnitest module"""

import unittest
from models.amenity import Amenity
import datetime

class AmenityTest(unittest.TestCase):
    """Suite of console test"""
    
    ame = Amenity()

    def test_ClassExist(self):
        """Test prove class exist"""

        clas = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.ame)), clas)

    def test_attributesexist(self):
        """Verify if attributtes exist"""

        self.assertTrue(hasattr(self.ame, 'name'))
        self.assertTrue(hasattr(self.ame, 'id'))
        self.assertTrue(hasattr(self.ame, 'created_at'))
        self.assertTrue(hasattr(self.ame, 'updated_at'))
            
if __name__ == '__main__':
    unittest.main()
