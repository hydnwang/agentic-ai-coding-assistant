import unittest
from get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_get_current(self):
        print("\nResult for current directory:")
        print(get_files_info("calculator", "."))
    
    def test_get_subdir(self):
        print("\nResult for pkg directory:")
        print(get_files_info("calculator", "pkg"))
    
    def test_get_not_existing(self):
        print("\nResult for /bin directory:")
        print(get_files_info("calculator", "/bin"))
    
    def test_get_out_of_range(self):
        print("\nResult for ../ directory:")
        print(get_files_info("calculator", "../"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
