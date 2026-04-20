import os
import unittest
from functions.write_file import write_file

class TestWriteFileContent(unittest.TestCase):
    def test_01_overwrite_existing_file(self):
        res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(res)

    def test_02_write_new_file(self):
        try:
            os.remove(os.path.normpath(os.path.join("calculator", "pkg/morelorem.txt")))
        except Exception as e:
            print(f'Warning: File deletion failed, {e}')
        res = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(res)
    
    def test_03(self):
        res = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(res)

if __name__ == "__main__":
    unittest.main(verbosity=1)