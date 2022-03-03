#!/usr/bin/python3
"""unittest module"""

import unittest
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    """Suite of console test"""

    my_model = BaseModel()

    def testBaseModel(self):
        """Test atributes value of a BaseModel instances"""

        self.my_model.name = "My First Model"
        self.my_model.my_number = "89"
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])

    if __name__ == '__main__':
        unittest.main()
