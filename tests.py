import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    
    def test_calculator(self):
        result = get_files_info("calculator", ".")
        correct = f"""Result for current directory:
- pkg: file_size=4096 bytes, is_dir=True
- main.py: file_size=575 bytes, is_dir=False
- tests.py: file_size=1342 bytes, is_dir=False"""
        
        self.assertEqual(result, correct)
        print(result)
        
    def test_calculator_pkg(self):
        result = get_files_info("calculator", "pkg")
        correct = f"""Result for 'pkg' directory:
- render.py: file_size=766 bytes, is_dir=False
- calculator.py: file_size=1737 bytes, is_dir=False"""
        self.assertEqual(result, correct)
        print(result)
        
    def test_calculator_bin(self):
        result = get_files_info("calculator", "/bin")
        correct = f"""Result for '/bin' directory:
Error: Cannot list "/bin" as it is outside the permitted working directory"""
        self.assertEqual(result, correct)
        print(result)
        
    def test_calculator_err(self):
        result = get_files_info("calculator", "../")
        correct = f"""Result for '../' directory:
Error: Cannot list "../" as it is outside the permitted working directory"""
        self.assertEqual(result, correct)
        print(result)
    


if __name__ == "__main__":
    unittest.main()