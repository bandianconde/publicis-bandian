from reader import Inputs
from reader import MowerInput
from reader import read_inputs
from utils import MowerPos
import pytest

from utils import move_mower
from pathlib import Path
import os.path as op


def test_reader():
    input_filename = Path(op.dirname(__file__)) / 'data' / 'input.txt'
    results = read_inputs(input_filename)
    expected = Inputs(
        max_x=5,
        max_y=5,
        mowers=[
            MowerInput(initial_x=1, initial_y=2, direction='N', instructions='GAGAGAGAA'),
            MowerInput(initial_x=3, initial_y=3, direction='E', instructions='AADAADADDA')
        ]
    )
    assert results == expected


@pytest.mark.parametrize(
    "current_mower_pos, max_x , max_y, action, expected",
    [
        (MowerPos(x=2, y=3, direction='N'), 5, 5, 'G', MowerPos(x=2, y=3, direction='W')),
        (MowerPos(x=2, y=3, direction='N'), 5, 5, 'D', MowerPos(x=2, y=3, direction='E')),

        (MowerPos(x=2, y=3, direction='E'), 5, 5, 'G', MowerPos(x=2, y=3, direction='N')),
        (MowerPos(x=2, y=3, direction='E'), 5, 5, 'D', MowerPos(x=2, y=3, direction='S')),

        (MowerPos(x=2, y=3, direction='W'), 5, 5, 'G', MowerPos(x=2, y=3, direction='S')),
        (MowerPos(x=2, y=3, direction='W'), 5, 5, 'D', MowerPos(x=2, y=3, direction='N')),

        (MowerPos(x=2, y=3, direction='S'), 5, 5, 'G', MowerPos(x=2, y=3, direction='E')),
        (MowerPos(x=2, y=3, direction='S'), 5, 5, 'D', MowerPos(x=2, y=3, direction='W')),

        (MowerPos(x=2, y=3, direction='W'), 5, 5, 'A', MowerPos(x=1, y=3, direction='W')),
        (MowerPos(x=2, y=3, direction='E'), 5, 5, 'A', MowerPos(x=3, y=3, direction='E')),
        (MowerPos(x=2, y=3, direction='S'), 5, 5, 'A', MowerPos(x=2, y=2, direction='S')),
        (MowerPos(x=2, y=3, direction='N'), 5, 5, 'A', MowerPos(x=2, y=4, direction='N')),


    ]
)
def test_move_mower(current_mower_pos: MowerPos,  max_x: int, max_y: int, action: str, expected: MowerPos):
    assert move_mower(current_mower_pos, max_x, max_y, action) == expected
