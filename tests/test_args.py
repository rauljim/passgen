from unittest import TestCase

from passgen import args


class Test(TestCase):
    def test_num_words(self):
        mock_argv = ['passgen', '-n', '22']
        options = args.get_cli_options(mock_argv)
        assert 22 == options.num_words
        mock_argv = ['passgen', '--num-words', '33']
        options = args.get_cli_options(mock_argv)
        assert 33 == options.num_words
        mock_argv = ['passgen']
        options = args.get_cli_options(mock_argv)
        assert args.DEFAULT_NUM_WORDS == options.num_words

    def test_count(self):
        mock_argv = ['passgen', '-c', '22']
        options = args.get_cli_options(mock_argv)
        assert 22 == options.count
        mock_argv = ['passgen', '--count', '33']
        options = args.get_cli_options(mock_argv)
        assert 33 == options.count
        mock_argv = ['passgen']
        options = args.get_cli_options(mock_argv)
        assert args.DEFAULT_COUNT == options.count

    def test_min_chars(self):
        mock_argv = ['passgen', '--min-chars', '33']
        options = args.get_cli_options(mock_argv)
        assert 33 == options.min_chars
        mock_argv = ['passgen']
        options = args.get_cli_options(mock_argv)
        assert args.DEFAULT_MIN_CHARS == options.min_chars

    def test_max_chars(self):
        mock_argv = ['passgen', '--max-chars', '33']
        options = args.get_cli_options(mock_argv)
        assert 33 == options.max_chars
        mock_argv = ['passgen']
        options = args.get_cli_options(mock_argv)
        assert args.DEFAULT_MAX_CHARS == options.max_chars

    def test_conflicting_min_max_chars(self):
        mock_argv = ['passgen', '--min-chars', '9999', '--max-chars', '11']
        options = args.get_cli_options(mock_argv)
        assert 9999 == options.min_chars
        assert args.DEFAULT_MAX_CHARS == options.max_chars

    def test_get_defaults(self):
        options = args.get_default_options()
        assert args.DEFAULT_COUNT == options.count
