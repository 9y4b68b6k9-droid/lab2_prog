import unittest
from regex_logic import find_tandem_words, check_word

class TestTandemRegex(unittest.TestCase):
    def test_check_word_positive(self):
        self.assertTrue(check_word("барабан"))
        self.assertTrue(check_word("колокол"))

    def test_check_word_negative(self):
        self.assertFalse(check_word("привет"))

    def test_find_tandem_words_in_text(self):
        text = "У дяди был барабан."
        found = find_tandem_words(text)
        self.assertIn("дяди", found)
        self.assertIn("барабан", found)

if __name__ == "__main__":
    unittest.main()