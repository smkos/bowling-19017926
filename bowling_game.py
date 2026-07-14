class Game:
    def __init__(self) -> None:
        self._rolls: list[int] = []

    def roll(self, pins: int) -> None:
        self._rolls.append(pins)

    def score(self) -> int:
        total = 0
        roll_index = 0

        for _ in range(10):
            if self._is_strike(roll_index):
                total += self._strike_score(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total += self._spare_score(roll_index)
                roll_index += 2
            else:
                total += self._frame_score(roll_index)
                roll_index += 2

        return total

    def _is_strike(self, roll_index: int) -> bool:
        return self._rolls[roll_index] == 10

    def _is_spare(self, roll_index: int) -> bool:
        return self._frame_score(roll_index) == 10

    def _strike_score(self, roll_index: int) -> int:
        return 10 + self._rolls[roll_index + 1] + self._rolls[roll_index + 2]

    def _spare_score(self, roll_index: int) -> int:
        return 10 + self._rolls[roll_index + 2]

    def _frame_score(self, roll_index: int) -> int:
        return self._rolls[roll_index] + self._rolls[roll_index + 1]
