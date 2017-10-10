import unittest
import grading
import pprint

class AverageTest(unittest.TestCase):

    def test_average(self):

        scores = { "Alice": [85, 76, 92, 88],
                     "Bob": [77, 88, 99, 55],
                   "Carol": [80, 80, 67, 90],
                    "Dave": [91, 92, 97, 90] }

        results = grading.assign_grades(scores)
        expected = {"Carol": "C", "Bob": "C", 'Dave': "A", "Alice": "B"}
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
