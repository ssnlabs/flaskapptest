import unittest
from main import add,sub

class TestApp(unittest.TestCase):
    def test_add(self):
        return self.assertEqual(add(5,3),8)
    def test_sub(self):
        return self.assertEqual(sub(5,3),2)


if __name__=="__main__":
    unittest.main()
