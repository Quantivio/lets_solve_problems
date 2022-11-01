# Leet Code Problem: Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/
# Complexity: Easy
# Description: Convert roman numeral to integer based on the given mapping.

"""
You may assume that the integer is not negative.
Example:
    Input: "III"
    Output: 3
    Because III = 3
"""
from time import perf_counter

mapping: dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


class RomanToInteger:
    @staticmethod
    def roman_to_int_loop_condition(roman: str) -> int:
        """
        Convert roman to integer using loop and condition with the help of mapping.
        """
        number: int = 0
        index = 0

        if len(roman) > 2:
            while index < len(roman):
                if roman[index] == "I" and index + 1 < len(roman) and (
                        roman[index + 1] == "V" or roman[index + 1] == "X"):
                    number += mapping[roman[index] + roman[index + 1]]
                    index += 2
                elif roman[index] == "X" and index + 1 < len(roman) and (
                        roman[index + 1] == "L" or roman[index + 1] == "C"):
                    number += mapping[roman[index] + roman[index + 1]]
                    index += 2
                elif roman[index] == "C" and index + 1 < len(roman) and (
                        roman[index + 1] == "D" or roman[index + 1] == "M"):
                    number += mapping[roman[index] + roman[index + 1]]
                    index += 2
                else:
                    number += mapping[roman[index]]
                    index += 1
        else:
            if roman in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                number = mapping[roman]
            else:
                if len(roman) == 2:
                    number = mapping[roman[0]] + mapping[roman[1]]
                if len(roman) == 1:
                    number = mapping[roman[0]]
        return number

    @staticmethod
    def roman_to_int_replace(roman: str) -> int:
        """
        Convert roman to integer using replace function with the help of mapping.
        """
        number = 0
        roman = roman.replace("IV", "IIII").replace("IX", "VIIII")
        roman = roman.replace("XL", "XXXX").replace("XC", "LXXXX")
        roman = roman.replace("CD", "CCCC").replace("CM", "DCCCC")
        for character in roman:
            number += mapping[character]
        return number


if __name__ == "__main__":
    start = perf_counter()
    output: int = RomanToInteger.roman_to_int_loop_condition("MMMXLV")
    print(output)
    end = perf_counter()
    print(f"Time taken with loops and condition: {end - start}")

    replace_start = perf_counter()
    output: int = RomanToInteger.roman_to_int_replace("MMMXLV")
    print(output)
    replace_end = perf_counter()
    print(f"Time taken with replace: {replace_end - replace_start}")
