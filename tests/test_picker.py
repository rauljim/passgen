from unittest import TestCase
import random

from passgen import picker


class TestPicker(TestCase):
    def test_basic(self):
        picker_generator = picker.make_picker_generator('abcdefg')
        picker._choice = random.choice  # monkey patch
        random.seed(42)  # deterministic 'random' generator
        self.assertEqual(list('faafc'), next(picker_generator))
        self.assertEqual(list('bbbfa'), next(picker_generator))
        self.assertEqual(list('ffeae'), next(picker_generator))
        self.assertEqual(list('daaab'), next(picker_generator))
