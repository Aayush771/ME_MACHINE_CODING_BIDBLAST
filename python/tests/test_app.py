import os
import contextlib
import unittest
import filecmp
from app import run

class TestApp(unittest.TestCase):

    def test_Application(self):
        # Arrange
        cwd = os.path.dirname(os.path.abspath(__file__))
        inputFile = os.path.join(cwd,"test_input_one.txt")
        arguments = ["-m app",f"INPUT_FILE={str(inputFile)}"]
        actualOutputFile = os.path.join(cwd,"test_input_one_actual_output.txt")
        expectedOutputFile = os.path.join(cwd,"test_input_one_expected_output.txt")
        # Act
        with open(actualOutputFile,'w') as f:
            with contextlib.redirect_stdout(f):
                run(arguments)
        # Assert
        self.assertTrue(filecmp.cmp(expectedOutputFile,actualOutputFile))



if __name__ == '__main__':
    unittest.main()