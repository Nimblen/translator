import unittest
from trans import translate

class TestTranslate(unittest.TestCase):

    def test_translate(self):
        input_text = "Hello, world!"
        expected_output_text = "Привет, мир!"
        output_text = translate(input_text)
        self.assertEqual(expected_output_text, output_text)

if __name__ == '__main__':
    unittest.main()