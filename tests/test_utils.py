import pytest

from utils import instructions_are_valid
from utils import positions_are_valid


@pytest.mark.parametrize(
    "x, y ,max_x, max_y, expected",
    [
        (2, 3, 5, 5, True),
        (0, 0, 1, 2, True),
        (0, 3, 1, 2, False),

    ]
)
def test_positions_are_valid(x, y, max_x, max_y, expected):
    assert positions_are_valid(x, y, max_x, max_y) is expected


@pytest.mark.parametrize(
    "instructions, expected",
    [
        ("GAGAGAGAA", True),
        ("AADAADADDA", True),
        ("ADGTAAAAGGG", False),

    ]
)
def test_instructions_are_valid(instructions, expected):
    assert instructions_are_valid(instructions) is expected
