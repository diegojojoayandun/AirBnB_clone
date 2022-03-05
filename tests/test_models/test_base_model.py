#!/usr/bin/python3
"""unittest module"""

import unittest
from models.base_model import BaseModel
import datetime


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

    def testsaveUpdate(self):
        """Checks if save method updates the instances update_at"""

        self.my_model.first_name = "Holberton"
        self.my_model.save()

        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

        first_dic = self.my_model.to_dict()

        self.my_model.first_name = "School"
        self.my_model.save()
        second_dic = self.my_model.to_dict()

        self.assertEqual(first_dic['created_at'], second_dic['created_at'])
        self.assertNotEqual(first_dic['updated_at'], second_dic['updated_at'])


if __name__ == '__main__':
    unittest.main()
