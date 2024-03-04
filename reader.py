from utils import Inputs
from exceptions import InvalidInputsInstruction
from exceptions import InvalidInputsPosition
from utils import MowerInput
from utils import instructions_are_valid
from utils import positions_are_valid


def read_inputs(filename: str) -> Inputs:
    """
        Read the file containing all the instructions for the mower
    :param filename: Path of the file
    :return: Inputs object for all the mower initial positions  and instructions
    """
    mowers = []
    with open(filename, 'r') as file_input:
        current_line = file_input.readline()
        max_x, max_y = (int(elt) for elt in current_line.split())
        while True:
            current_line = file_input.readline().strip('\n')
            if not current_line:
                break
            x, y, direction = current_line.split(' ')
            x, y = int(x), int(y)
            if not positions_are_valid(x, y, max_x, max_y):
                raise InvalidInputsPosition(f'Position x: {x}, y: {y} is invalid')
            instructions = file_input.readline().strip('\n')
            if not instructions_are_valid(instructions):
                raise InvalidInputsInstruction(f'These set of instructions is wrong: {instructions}')
            mowers.append(MowerInput(initial_x=x, initial_y=y, direction=direction, instructions=instructions))
    return Inputs(max_x=max_x, max_y=max_y, mowers=mowers)
