# Leet Code Problem: Remove Adjacent Duplicates in String
# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Complexity: Easy
# Description: Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent
# and equal letters, and removing them.

"""
Example:
    Input: "abbaca"
    Output: "ca"
    Explanation: For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal,
    and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is
    possible, so the final string is "ca".
"""

from time import perf_counter


class RemoveAdjacentDuplicates:
    @staticmethod
    def solution(base_string: str) -> str:
        stack = []
        for character in base_string:
            if stack and stack[-1] == character:
                stack.pop()
            else:
                stack.append(character)
        return "".join(stack)


if __name__ == "__main__":
    start_time = perf_counter()
    print(RemoveAdjacentDuplicates.solution("abbaca"))
    end_time = perf_counter()
    print(f"The time taken {end_time - start_time}")
