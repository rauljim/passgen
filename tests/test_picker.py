import itertools
from unittest import TestCase
import random

from passgen import picker, args


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
        options = args.get_default_options()
        options.num_words = 9999
        picker_generator = picker.make_picker_generator('abc', options)
        assert 9999 == len(next(picker_generator))

    def test_picking_from_empty(self):
        picker_generator = picker.make_picker_generator([])
        with self.assertRaises(StopIteration):
            next(picker_generator)

        picker_generator = picker.make_picker_generator([])
        for picked_words in itertools.islice(picker_generator, 3):
            print(picked_words)
