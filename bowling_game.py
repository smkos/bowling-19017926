class Game:
    def __init__(self) -> None:
        self._rolls: list[int] = []

    def roll(self, pins: int) -> None:
        self._rolls.append(pins)

    def score(self) -> int:
        total = 0
        roll_index = 0

        for _ in range(10):
            if self._is_spare(roll_index):
                total += 10 + self._rolls[roll_index + 2]
                roll_index += 2
            else:
                total += self._rolls[roll_index] + self._rolls[roll_index + 1]
                roll_index += 2

        return total

    def _is_spare(self, roll_index: int) -> bool:
        return self._rolls[roll_index] + self._rolls[roll_index + 1] == 10
