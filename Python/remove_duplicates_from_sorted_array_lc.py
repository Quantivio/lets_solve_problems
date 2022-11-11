# Leet Code Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Complexity: Easy
# Description: Given a sorted array nums, remove the duplicates in-place such that each element appear
# only once and return the new length.

"""
Example:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2]
    Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
"""

from collections import Counter
from time import perf_counter


class RemoveDuplicatesFromSortedArray:
    @staticmethod
    def solution_with_stack(array: list[int]) -> int:
        """This will work but not provide the exact solution"""
        stack = []
        array_copy = array.copy()
        for number in array_copy:
            if stack and number in stack:
                array.remove(number)
            else:
                stack.append(number)
        print(stack)
        return len(stack)

    @staticmethod
    def solution_with_counter(nums: list[int]) -> int:
        number_count_dict = Counter(nums)
        counter = 0
        for i in number_count_dict:
            nums[counter] = i
            counter += 1
        return len(number_count_dict)

    @staticmethod
    def solution_with_for_loop(array: list[int]) -> int:
        current_index = 0
        for index in range(len(array)):
            if index > 0 and array[index] == array[index - 1]:
                index += 1
            else:
                array[current_index] = array[index]
                current_index += 1
        return current_index


if __name__ == "__main__":
    start = perf_counter()
    print(RemoveDuplicatesFromSortedArray.solution_with_stack([1, 1, 2]))
    end = perf_counter()
    print(f"Time taken with stack: {end - start}")

    start = perf_counter()
    print(RemoveDuplicatesFromSortedArray.solution_with_counter([1, 1, 2]))
    end = perf_counter()
    print(f"Time taken with counter: {end - start}")

    start = perf_counter()
    print(RemoveDuplicatesFromSortedArray.solution_with_for_loop([1, 1, 2]))
    end = perf_counter()
    print(f"Time taken with for loop logic: {end - start}")
