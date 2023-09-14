import unittest
from circles import circle_area
from math import pi

class CircleArea(unittest.TestCase):
    def test_area(self):
        #tests area when radius is >= 0.
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*(2.1**2))

    def test_values(self):
        #tests and raises value error
        self.assertRaises(ValueError, circle_area, -2)

    def test_type(self):
        #make sure type error are raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
