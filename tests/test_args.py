from unittest import TestCase

from passgen import args


class Test(TestCase):
    def test_count(self):
        mock_argv = ['passgen', '-C', '2']
        options = args.get_cli_options(mock_argv)
        assert 2 == options.count
        mock_argv = ['passgen', '--count', '2']
        options = args.get_cli_options(mock_argv)
        assert 2 == options.count
        mock_argv = ['passgen']
        options = args.get_cli_options(mock_argv)
        assert 5 == options.count
