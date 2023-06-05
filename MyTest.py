import unittest
import UnitTestMain as utm

class MyTestCase(unittest.TestCase):
    def test_my_functionAdd(self):
        #self.assertTrue()
        #self.assertFalse()
        self.assertEqual(utm.myfunctionAdd(2, 5), 7)
        self.assertEqual(utm.myfunctionAdd(2, 3), 5)
    def test_my_functionMul(self):
        self.assertEqual(utm.myfunctionMultiply(2, 5), 10)
        self.assertEqual(utm.myfunctionMultiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()

