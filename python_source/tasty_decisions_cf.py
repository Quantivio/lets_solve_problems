# Leet Code Problem: Tasty Decisions
# Link: https://www.codechef.com/submit/TASTEDEC
# Complexity: Easy
# Description: Find whether chocolate is tasty or candy is tasty based on given inputs.

"""
Example:
    Input:
        TotalTestCase(n): 4
            TestCase1: 5 1
            TestCase2: 5 2
            TestCase3: 5 3
            TestCase4: 3 10
    Output:
        Chocolate
        Either
        Candy
        Candy
    Explanation: 1. Chocolate is tasty for 1st test case because 5 * 2(each chocolate packet contains two bars) = 10
    and 5(Each packet of candy has 5 pieces) * 1 = 5,
"""

from time import perf_counter


class TastyDecisions:
    @staticmethod
    def solution():
        total_test_cases = int(input())
        for _ in range(total_test_cases):
            items = [int(item) for item in input().split()]
            if 2 * items[0] > 5 * items[1]:
                print("Chocolate")
            elif 2 * items[0] < 5 * items[1]:
                print("Candy")
            elif 2 * items[0] == 5 * items[1]:
                print("Either")


if __name__ == "__main__":
    start = perf_counter()
    TastyDecisions.solution()
    end = perf_counter()
    print(f"Time taken: {end - start}")
