"""
SampleTest
"""
from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module """
    def test__add(self):
        """Test adding number together"""
        res = calc.add(5,6)
        self.assertEqual(res, 11)

    def test__substract(self):
        """Substract y and x and return result"""

        res = calc.substract(10,15)

        self.assertEqual(res, 5)