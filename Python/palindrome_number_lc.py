# Leet Code Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Complexity: Easy
# Description: Determine whether an integer is a palindrome. An integer is a palindrome when it reads from rtl.

"""
You may assume that the integer is not negative.
Example:
    Input: 121
    Output: true
    Because 121 reads the same from rtl as from ltr.
"""
from time import perf_counter


class PalindromNumber:
    @staticmethod
    def palindrome_without_string_function(number: int):
        """
        This method will check if the number is a palindrome without using string function.
        """
        if str(number) == str(number)[::-1]:
            return True
        return False

    @staticmethod
    def palindrome_with_reversed_function(number: int):
        """
        This method will check if the number is a palindrome using reversed function.
        """
        if str(number) == "".join(reversed(str(number))):
            return True
        return False

    @staticmethod
    def palindrome_with_loop(number: int):
        """
        This method will check if the number is a palindrome using loop.
        """
        number = str(number)
        for index in range(len(number) // 2):  # Not required to run the complete loop
            if number[index] != number[-(index + 1)]:
                return False
        return True


if __name__ == "__main__":
    start = perf_counter()
    print(
        "Result with indexing", PalindromNumber.palindrome_without_string_function(121)
    )
    end = perf_counter()
    print(f"Time taken with indexing: {end - start}")

    recursion_start = perf_counter()
    print(
        "Result with reversed function",
        PalindromNumber.palindrome_with_reversed_function(121),
    )
    recursion_end = perf_counter()

    print(f"Time taken with reversed function: {recursion_end - recursion_start}")

    enumerate_start = perf_counter()
    print("Result with loop", PalindromNumber.palindrome_with_loop(121))
    enumerate_end = perf_counter()

    print(f"Time taken with loop: {enumerate_end - enumerate_start}")
