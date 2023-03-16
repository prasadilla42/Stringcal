import unittest
from utils import Handlers

class TestExtractNumbersFromString(unittest.TestCase):

    def setUp(self):
        self.instance = Handlers()

    def test_extract_numbers_from_string(self):
        input_string = "The temperature is -3 degrees Celsius and the wind speed is 10 km/h."
        expected_output = [-3, 10]
        self.assertEqual(self.instance._extract_numbers_from_string(input_string), expected_output)

    def test_extract_numbers_from_string_empty_input(self):
        input_string = ""
        expected_output = []
        self.assertEqual(self.instance._extract_numbers_from_string(input_string), expected_output)

    def test_extract_numbers_from_string_no_numbers(self):
        input_string = "There are no numbers in this string."
        expected_output = []
        self.assertEqual(self.instance._extract_numbers_from_string(input_string), expected_output)

    def test_extract_numbers_from_string_decimal_numbers(self):
        input_string = "The price is -3.14 dollars and the discount is 10.5%."
        expected_output = [-3,14,10,5]
        self.assertEqual(self.instance._extract_numbers_from_string(input_string), expected_output)

if __name__ == '__main__':
    unittest.main()
