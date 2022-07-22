from unittest import TestCase
import bad


class TestBad(TestCase):
    def test_random_english_alphabets_generator_returns_26_english_alphabets(self):
        alphabets = bad.random_english_alphabets_generator()

        self.assertEqual(len(alphabets), 26)

    def test_random_english_alphabets_generator_returns_unique_26_characters(self):
        alphabets = bad.random_english_alphabets_generator()

        self.assertEqual(len("".join(set(alphabets))), 26)

    def test_random_english_alphabets_generator_returns_lowercase_alphabets(self):
        alphabets = bad.random_english_alphabets_generator()

        self.assertEqual(alphabets, alphabets.lower())

    def test_random_english_alphabets_generator_random_alphabets_everytime(self):
        alphabets = bad.random_english_alphabets_generator()
        some_different_alphabets = bad.random_english_alphabets_generator()

        self.assertNotEqual(alphabets, some_different_alphabets)
