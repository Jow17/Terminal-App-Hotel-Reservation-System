import unittest
from main import pin_generator  
from io import StringIO
from main import home  
from unittest.mock import patch


# Test case for pin generation
class TestPinGenerator(unittest.TestCase):
    def test_generated_pin_in_range(self):
        pin = pin_generator()
        self.assertTrue(1000 <= pin <= 9999, f"Generated PIN {pin} is not within the expected range.")

if __name__ == '__main__':
    unittest.main()

# Test Case for home function 
class TestHomeFunction(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_home(self, mock_stdout):
        # Simulate user input by providing '1' as input.
        with patch("builtins.input", side_effect=['1']):
            home()

        # Check the printed output
        expected_output = "Welcome to Atlas Hotel!\nLogin: 1 | Create a new account: 2\n\n-> "
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()