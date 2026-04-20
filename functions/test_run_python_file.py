import os
import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_01_run_without_args(self):
        res = run_python_file("calculator", "main.py")
        print(res)
    
    def test_02_run_with_args(self):
        res = run_python_file("calculator", "main.py", ["3 + 5"])
        print(res)
    
    def test_03_run_tests(self):
        res = run_python_file("calculator", "tests.py")
        print(res)
    
    def test_04_run_outside_working_dir(self):
        res = run_python_file("calculator", "../main.py")
        print(res)
    
    def test_05_run_nonexistent_file(self):
        res = run_python_file("calculator", "nonexistent.py")
        print(res)
    
    def test_06_run_non_python_file(self):
        res = run_python_file("calculator", "lorem.txt")
        print(res)


if __name__ == "__main__":
    unittest.main(verbosity=0)