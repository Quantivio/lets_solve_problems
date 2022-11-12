# Code Chef Problem: Equal Distribution
# Link: https://www.codechef.com/submit/EQUALDIST
# Complexity: Easy
# Description: Return yes or no if given eatables can be distributed equally among bob and alice.


"""
Example:
    Input:
        TotalTestCases = 2
        TestCase1: 1 1
        TestCase2: 1 3
    Output:
        Yes
        Yes
    Explanation: In the first test case, bob and alice can eat 1 and 1 eatables respectively.
    In the second test case, bob and alice can eat 1 and 3 eatables respectively so alice can give one eatable to
    bob to nake it distributed.
"""


class EqualDistribution:
    @staticmethod
    def solution():
        total_test_cases: int = int(input())
        for _ in range(total_test_cases):
            bob, alice = map(int, input().split())
            total = bob + alice
            if total % 2 == 0:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    EqualDistribution.solution()
