from unittest import TestCase
import random

from passgen.picker import Picker


class TestPicker(TestCase):
    def test_basic(self):
        picker = Picker('abcdefg')
        picker._Picker__choice = random.choice  # monkey patch
        random.seed(42)  # deterministic 'random' generator
        self.assertEqual(list('faafc'), picker.pick())
        self.assertEqual(list('bbbfa'), picker.pick())
        self.assertEqual(list('ffeae'), picker.pick())
        self.assertEqual(list('daaab'), picker.pick())
