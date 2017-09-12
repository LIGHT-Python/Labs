import unittest
import week1

class TestWeek1(unittest.TestCase):

    def test_add_works(self):
        self.assertEqual(4, week1.add(2, 2))

    def test_adding_without_numbers_causes_error(self):
        self.assertRaises(TypeError, week1.add, 2, '2')

    def test_sub_works(self):
        self.assertEquals(4, week1.sub(8, 5))

    def test_mul_works(self):
        self.assertEquals(20, week1.mul(4, 5))

    def test_div_works(self):
        self.assertEquals(10, week1.div(100, 10))

if __name__ == '__main__':
    unittest.main()

