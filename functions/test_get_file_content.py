import unittest
from functions.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
    def test_01_larger_than_10k_char(self):
        res = get_file_content("calculator", "lorem.txt")
        print(f'file size: {len(res)}')
        print(f'last message: {res[-51:]}')
    
    def test_02_current_dir_valid_file(self):
        res = get_file_content("calculator", "main.py")
        print(f'file size: {len(res)}')
        print(f'file content: {res}')
    
    def test_03_subdir_valid_file(self):
        res = get_file_content("calculator", "pkg/calculator.py")
        print(f'file size: {len(res)}')
        print(f'file content: {res}')
    
    def test_04_invalid_file_path(self):
        res = get_file_content("calculator", "/bin/cat")
        print(f'file size: {len(res)}')
        print(f'file content: {res}')
    
    def test_05_nonexistent_file(self):
        res = get_file_content("calculator", "pkg/does_not_exist.py")
        print(f'file size: {len(res)}')
        print(f'file content: {res}')

if __name__ == "__main__":
    unittest.main(verbosity=1)