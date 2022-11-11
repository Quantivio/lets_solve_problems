# Leet Code Problem: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Complexity: Hard
# Description: There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.

"""
Example:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
"""


class MedianOfTwoSortedArrays:
    @staticmethod
    def solution(array_one: list[int], array_two: list[int]) -> float:
        extended_array = array_one + array_two
        extended_array.sort()
        index = len(extended_array) // 2
        if len(extended_array) % 2 == 0:
            return (extended_array[index] + extended_array[index - 1]) / 2
        else:
            return extended_array[index]


print(MedianOfTwoSortedArrays.solution([1, 3], [2]))
