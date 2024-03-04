from pathlib import Path
import os.path as op

from main import game


def test_game():
    input_filename = Path(op.dirname(__file__)) / 'data' / 'input.txt'
    result_filename = Path(op.dirname(__file__)) / 'data' / 'results.txt'
    game(input_filename, result_filename)
    expected = "1 3 N\n5 1 E\n"
    with open(result_filename, 'r') as result_file:
        assert result_file.read() == expected
