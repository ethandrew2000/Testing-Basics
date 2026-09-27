import unittest

from challenge import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_palindrome_word(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome_word(self):
        self.assertFalse(is_palindrome("hello"))

    def test_ignores_capitalization(self):
        self.assertTrue(is_palindrome("RaceCar"))

    def test_ignores_spaces(self):
        self.assertTrue(is_palindrome("nurses run"))

    def test_ignores_punctuation_in_phrase(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))

    def test_numeric_palindrome(self):
        self.assertTrue(is_palindrome("12321"))

    def test_digits_are_not_discarded(self):
        self.assertFalse(is_palindrome("1a2"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_only_punctuation_and_whitespace(self):
        self.assertTrue(is_palindrome(" \t!?\n"))

    def test_single_character(self):
        self.assertTrue(is_palindrome("x"))


if __name__ == "__main__":
    unittest.main()
