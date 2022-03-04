#!/usr/bin/python3
"""unnitest module"""

import unittest
from models.state import State
import datetime


class StateTest(unittest.TestCase):
    """Suite of console test"""

    st = State()

    def test_ClassExist(self):
        """Test prove class exist"""

        clas = "<class 'models.state.State'>"

        self.assertEqual(str(type(self.st)), clas)

    def test_AtributeExist(self):
        """Verify if attributtes exist"""

        self.assertTrue(hasattr(self.st, 'name'))
        self.assertTrue(hasattr(self.st, 'id'))
        self.assertTrue(hasattr(self.st, 'created_at'))
        self.assertTrue(hasattr(self.st, 'updated_at'))

    def test_CorrectType(self):
        """Verify if the type of the attribute is correct"""

        self.assertIsInstance(self.st.name, str)
        self.assertIsInstance(self.st.id, str)
        self.assertIsInstance(self.st.created_at, datetime.datetime)
        self.assertIsInstance(self.st.updated_at, datetime.datetime)

    def test_inheritance(self):
        """Verify if state is subclass from BaseModel"""

        self.assertIsInstance(self.st, State)


if __name__ == '__main__':
    unittest.main()
