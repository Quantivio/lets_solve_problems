# Leet Code Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Complexity: Easy
# Description: Determine whether given set of parentheses is valid.
"""
You may assume that the integer is not negative.
Example:
    Input: {[]}
    Output: true
    Because {[]} is a valid set of parentheses because each set of parentheses close each other.
"""

from time import perf_counter


class ValidParentheses:
    @staticmethod
    def valid_parentheses(string: str) -> bool:
        bracket_list = []
        bracket_mappings = {
            "(": ")",
            "{": "}",
            "[": "]",
            "<": ">",
        }
        for char in string:
            if char in "({[":  # change to '([{' for better performance
                bracket_list.append(char)
            elif not bracket_list or bracket_mappings[bracket_list.pop()] != char:
                return False

        return not bracket_list


if __name__ == "__main__":
    start_timer = perf_counter()
    print(ValidParentheses.valid_parentheses("{[]}"))
    end_timer = perf_counter()
    print(f"Time taken {end_timer - start_timer}")
