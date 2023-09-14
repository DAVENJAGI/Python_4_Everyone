import unittest
from calculator import Calculator 

class TestClass(unittest.TestCase):

    def test_add(self):
        result = Calculator(10, 5)
        self.assertEqual(result, 15)

if __name__ == "__main__":
    unittest.main()
