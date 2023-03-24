SECRET = 6


def guess(num: int):
    if num == SECRET:
        return 0
    elif num < SECRET:
        return -1
    else:
        return 1


class Solution:
    def __init__(self):
        self.initial_index = 0
        self.final_index = 0

    def guess_number(self, limit: int) -> int:
        if self.final_index == 0:
            self.final_index = limit
        for number in range(self.initial_index, self.final_index):
            if guess(number) == 0:
                return number
            elif guess(number) == -1:
                self.initial_index = number
            else:
                self.final_index = number

    @staticmethod
    def guess_number_for_loop(limit: int) -> int:
        for number in range(0, limit + 1):
            if guess(number) == 0:
                return number
        return limit


solution = Solution()

print(solution.guess_number(10))
print(solution.guess_number_for_loop(10))
