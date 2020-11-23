from unittest import TestCase
import random

from passgen import picker


class TestPicker(TestCase):
    def test_basic(self):
        picker_generator = picker.make_picker_generator('abcdefg')
        original_choice = picker._choice  # TODO: use a context manager here?
        picker._choice = random.choice  # monkey patch secrets.choice
        random.seed(42)  # 'random' generator for deterministic testing
        self.assertEqual(list('faafc'), next(picker_generator))
        self.assertEqual(list('bbbfa'), next(picker_generator))
        self.assertEqual(list('ffeae'), next(picker_generator))
        self.assertEqual(list('daaab'), next(picker_generator))
        picker._choice = original_choice

    def test_num_words_greater_than_words_in_dictionary(self):
        picker_generator = picker.make_picker_generator('abc', 9999)
        assert 9999 == len(next(picker_generator))
