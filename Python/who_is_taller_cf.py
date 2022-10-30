# Code Chef Problem: Who is taller
# Link: https://www.codechef.com/submit/TALLER
# Complexity: Easy
# Description: Given the heights of two persons, you need to tell who is taller.

"""
Example:
    Input: 1 2
    Output: B
"""

from time import perf_counter


class WhoIsTaller:
    @staticmethod
    def solution():
        total_test_cases: int = int(input())
        index = 0
        while index < total_test_cases:
            index += 1
            a_height, b_height = map(int, input().split())
            if a_height > b_height:
                print("A")
            else:
                print("B")


if __name__ == "__main__":
    start_time = perf_counter()
    WhoIsTaller.solution()
    end_time = perf_counter()
    print(f"Time taken: {end_time - start_time} seconds")
