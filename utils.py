import dataclasses
from typing import List


@dataclasses.dataclass
class MowerInput:
    """
        Mower Input for each mower
    """
    initial_x: int
    initial_y: int
    direction: str
    instructions: str


@dataclasses.dataclass
class MowerPos:
    """
        Mower Position and Direction
    """
    x: int
    y: int
    direction: str


@dataclasses.dataclass
class Inputs:
    """
        Results of reading input files
    """
    max_x: int
    max_y: int
    mowers: List[MowerInput]


def positions_are_valid(x: int, y: int, max_x: int, max_y: int):
    """
        Make sure positions are valid
    :param x:
    :param y:
    :param max_x:
    :param max_y:
    :return: True if valid False otherwise
    """
    return (0 <= x <= max_x) and (0 <= y <= max_y)


def instructions_are_valid(instructions: str):
    """
        Check if all actions of instructions are in ('A', 'G', 'D')
    :param instructions: all the instructions
    :return: True if valid False otherwise
    """
    for instr in instructions:
        if instr not in ('A', 'G', 'D'):
            return False
    return True


mapping_directions = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}


def move_mower(mower_pos: MowerPos, max_x: int, max_y: int, action: str) -> MowerPos:
    """
        Move mower depending on current position, current direction and action
    :param mower_pos: Current Mower Pos
    :param max_x: Max x
    :param max_y: Max y
    :param action: action to apply
    :return: MowerPos object representing the next state of the mower
    """
    directions = ['N', 'E', 'S', 'W']
    current_x = mower_pos.x
    current_y = mower_pos.y
    current_direction = mower_pos.direction
    delta = mapping_directions[current_direction]
    current_direction_pos = directions.index(current_direction)
    if action == 'G':
        current_direction = directions[current_direction_pos - 1]
    elif action == 'D':
        current_direction = directions[(current_direction_pos + 1) % 4]
    elif action == 'A':
        next_x = current_x + delta[0]
        next_y = current_y + delta[1]
        if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
            current_x = next_x
            current_y = next_y
    return MowerPos(x=current_x, y=current_y, direction=current_direction)
