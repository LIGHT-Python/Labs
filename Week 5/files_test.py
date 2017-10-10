import unittest
import files
import os.path

class FilesTest(unittest.TestCase):

    def test_read_file(self):
        count = files.count_lines("declaration.txt")

        self.assertEqual(154, count)

    def test_write_file(self):
        fn = "hello.txt"
        files.write_file(fn)

        self.assertTrue(os.path.exists(fn))

        lines = None
        with open(fn, "rb") as f:
            lines = f.readlines()

        self.assertTrue( len(lines) > 1 )

if __name__ == '__main__':
    unittest.main()


