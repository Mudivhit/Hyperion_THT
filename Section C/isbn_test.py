import unittest
import isbn


class MyTestCase(unittest.TestCase):

    def test_valid_isbn_10(self):
        
        number = "0943396042"
        result = isbn.verify_isbn10(number)
        self.assertEqual(result,"Valid")

    def test_invalid_isbn_10(self):
        
        number = "9783161484"
        result = isbn.verify_isbn10(number)
        self.assertEqual(result,"Invalid")

    def test_valid_isbn_13(self):

        number = "9783161484100"
        result = isbn.verify_isbn13(number)
        self.assertEqual(result,"Valid")
        
    
    def test_invalid_isbn_13(self):

        number = "9999999999999"
        result = isbn.verify_isbn13(number)
        self.assertEqual(result,"Invalid")
    
    def test_isbn_10_conversion(self):
        
        number = "0943396042"
        answer = "9780943396040"
        result = isbn.convert_isbn10(number)
        self.assertEqual(result,answer)
    