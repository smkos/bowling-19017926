FRAMES_PER_GAME = 10
ROLLS_PER_STRIKE_FRAME = 1
ROLLS_PER_OPEN_OR_SPARE_FRAME = 2


class Game:
    def __init__(self) -> None:
        self._rolls: list[int] = []

    def roll(self, pins: int) -> None:
        self._rolls.append(pins)

    def score(self) -> int:
        total = 0
        first_roll_of_frame = 0

        for _ in range(FRAMES_PER_GAME):
            if self._is_strike(first_roll_of_frame):
                total += self._strike_score(first_roll_of_frame)
                first_roll_of_frame += ROLLS_PER_STRIKE_FRAME
            elif self._is_spare(first_roll_of_frame):
                total += self._spare_score(first_roll_of_frame)
                first_roll_of_frame += ROLLS_PER_OPEN_OR_SPARE_FRAME
            else:
                total += self._frame_score(first_roll_of_frame)
                first_roll_of_frame += ROLLS_PER_OPEN_OR_SPARE_FRAME

        return total

    def _is_strike(self, first_roll_of_frame: int) -> bool:
        return self._rolls[first_roll_of_frame] == 10

    def _is_spare(self, first_roll_of_frame: int) -> bool:
        return self._frame_score(first_roll_of_frame) == 10

    def _strike_score(self, first_roll_of_frame: int) -> int:
        next_two_rolls = slice(first_roll_of_frame + 1, first_roll_of_frame + 3)
        return 10 + sum(self._rolls[next_two_rolls])

    def _spare_score(self, first_roll_of_frame: int) -> int:
        bonus_roll = first_roll_of_frame + 2
        return 10 + self._rolls[bonus_roll]

    def _frame_score(self, first_roll_of_frame: int) -> int:
        first_roll, second_roll = first_roll_of_frame, first_roll_of_frame + 1
        return self._rolls[first_roll] + self._rolls[second_roll]
