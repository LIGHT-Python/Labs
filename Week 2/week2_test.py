import unittest

class TestWeek2(unittest.TestCase):

    def test_variables_add(self):
        x = 2
        y = 4
        self.assertEqual(6, x + y)

    def test_variables_mul(self):
        y = 4
        x = 2

        self.assertEqual(8, x * y)

    def test_variables_sub(self):
        x = 2
        y = 4

        self.assertEqual(-2, x - y)

    def test_variables_str(self):
        x = "Alfred"
        y = "Batman"

        self.assertEqual("Alfred is Batman's butler.",
                "{0} is {1}'s butler.".format(x, y))

    def test_if_true(self):
        x = None
        y = True

        if y:
            x = 42

        self.assertEqual(42, x)

    def test_if_batman(self):
        butler = None
        superhero = "Batman"

        if superhero == "Batman":
            butler = "Alfred"

        self.assertEqual("Alfred", butler)


    def test_if_false(self):
        x = None

        if False:
            x = 42
        else:
            x = 10

        self.assertEqual(10, x)

    def test_elif(self):
        x = None

        if False:
            x = 42
        elif 'foo':
            x = 17
        else:
            x = 10

        self.assertEqual(17, x)

if __name__ == '__main__':
    unittest.main()

