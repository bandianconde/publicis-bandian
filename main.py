from pathlib import Path
from typing import Union

from mower import Mower
from reader import read_inputs
import argparse


def game(input_filename: Union[Path, str], result_filename: Union[str, Path]):
    """
       Main function to generate results in a file for a given input file
    :param input_filename: filename for the all mowers inputs
    :param result_filename: filename for the results
    :return:
    """
    final_positions = []
    inputs = read_inputs(input_filename)
    for mower_input in inputs.mowers:
        mower = Mower(inputs.max_x, inputs.max_y)
        final_mower_pos = mower.get_final_positions(mower_input)
        final_positions.append(final_mower_pos)

    with open(result_filename, 'w') as result_file:
        for position in final_positions:
            result_file.write(f'{position.x} {position.y} {position.direction}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This script does something.")
    parser.add_argument("input_filename", help="Input filename")
    parser.add_argument("result_filename", help="Result filename")
    args = parser.parse_args()
    input_filename = args.input_filename
    result_filename = args.result_filename
    game(input_filename, result_filename)
