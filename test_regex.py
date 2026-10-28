import unittest
from main import find_tandem_words, check_word

class TestTandemRegex(unittest.TestCase):
    def test_check_word_positive(self):
        self.assertTrue(check_word("мама"))
        self.assertTrue(check_word("папа"))
        self.assertTrue(check_word("дядя"))

    def test_check_word_negative(self):
        self.assertFalse(check_word("привет"))
        self.assertFalse(check_word("тандем"))

    def test_find_tandem_words_in_text(self):
        text = "У дяди был барабан и колокол. Мама мыла раму."
        found = find_tandem_words(text)
        self.assertIn("мама", found)

if __name__ == "__main__":
    unittest.main()