import unittest
from main import pin_generator  # Replace 'your_module' with the actual module name

class TestPinGenerator(unittest.TestCase):
    def test_pin_generator(self):
        room_pin = []
        pin_generator(room_pin)
        
        # Verify that the generated PIN is within the specified range
        generated_pin = room_pin[0]
        self.assertTrue(1000 <= generated_pin <= 9999)

if __name__ == '__main__':
    unittest.main()