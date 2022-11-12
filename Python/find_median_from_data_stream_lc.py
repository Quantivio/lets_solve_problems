# Leet Code Problem: Find Median from Data Stream
# Link: https://github.com/pythonhubdev/lets_solve_problems
# Complexity: easy
# Description: Find the median of a stream of integers.

"""
Example:
    Input: [2,3,4,5, 8, 9 , 1]
    Output: 1.00000
"""


class FindMedianFromDataStream:
    def __init__(self):
        self.array = []

    def add_num(self, num):
        self.array.append(num)

    def find_median(self):
        self.array.sort()
        index = len(self.array) // 2
        if len(self.array) % 2 == 0:
            return (self.array[index] + self.array[index - 1]) / 2
        else:
            return self.array[index]
