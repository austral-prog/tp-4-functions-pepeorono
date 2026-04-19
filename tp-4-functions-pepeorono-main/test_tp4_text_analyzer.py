import unittest
import text_analyzer as ex6


class TP4TextAnalyzerCases(unittest.TestCase):

    def test_total_letters(self):
        self.assertEqual(4, ex6.total_letters("hola"))
        self.assertEqual(9, ex6.total_letters("hola mundo"))
        self.assertEqual(0, ex6.total_letters("123"))

    def test_vowel_percentage(self):
        self.assertEqual(50.0, ex6.vowel_percentage("hola"))
        self.assertEqual(100.0, ex6.vowel_percentage("aeiou"))
        self.assertEqual(0.0, ex6.vowel_percentage("rhythm"))
        self.assertEqual(0.0, ex6.vowel_percentage("123"))

    def test_analyze_text(self):
        self.assertEqual("V:2 C:2 T:4 P:50.0%", ex6.analyze_text("hola"))
        self.assertEqual("V:4 C:5 T:9 P:44.4%", ex6.analyze_text("hola mundo"))
        self.assertEqual("V:5 C:0 T:5 P:100.0%", ex6.analyze_text("aeiou"))

    def test_analyze_text_empty_letters(self):
        self.assertEqual("V:0 C:0 T:0 P:0.0%", ex6.analyze_text("123"))

    def test_analyze_text_mixed(self):
        # "Python 3" → P,y,t,h,o,n = 6 letters, vowel=o=1, consonants=5
        self.assertEqual("V:1 C:5 T:6 P:16.7%", ex6.analyze_text("Python 3"))


if __name__ == '__main__':
    unittest.main()
