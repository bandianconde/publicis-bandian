from utils import MowerInput
from utils import MowerPos
from utils import move_mower


class Mower:
    """
        Class representing a Mower
    """

    def __init__(self, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y
        self.current_pos = None

    def move(self, action: str):
        """
            Move a mower depending on action
        :param action:
        :return:
        """
        next_mower_pos = move_mower(
            self.current_pos,
            self.max_x,
            self.max_y,
            action
        )
        self.current_pos = next_mower_pos

    def get_final_positions(self, mower_input: MowerInput) -> MowerPos:
        """

        :param mower_input:
        :return:
        """
        self.current_pos = MowerPos(x=mower_input.initial_x, y=mower_input.initial_y, direction=mower_input.direction)
        instructions = mower_input.instructions
        for action in instructions:
            self.move(action)
        return self.current_pos
