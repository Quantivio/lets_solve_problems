# Leet Code Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Complexity: Easy
import sys
from time import perf_counter

sys.setrecursionlimit(100000)


class TwoSum:
    @staticmethod
    def two_sums_solution_for_loop(numbers: list[int], target: int) -> list[int]:

        """
        This method has two for loops for keeping the value from initial for loop and adding it with
        the other value in the list. This solution will only work for smaller list. Will throw time
        limit exceeded error for other larger list.
        """
        for index in range(len(numbers)):
            for nested_index in range(index + 1, len(numbers)):
                if numbers[index] + numbers[nested_index] == target:
                    return [index, nested_index]
        return []

    @staticmethod
    def two_sums_recursion(numbers: list[int], target: int) -> list[int]:
        """
        This method uses recursion to find the two numbers that add up to the target.
        Will throw recursion error for larger list or time limit exceeded error.
        """

        def two_sums_recursion_helper(index: int) -> list[int]:
            if index == len(numbers):
                return []
            for nested_index in range(index + 1, len(numbers)):
                if numbers[index] + numbers[nested_index] == target:
                    return [index, nested_index]
            return two_sums_recursion_helper(index + 1)

        return two_sums_recursion_helper(0)

    @staticmethod
    def two_sums_enumerate(numbers: list[int], target: int) -> list[int]:
        """
        This method uses enumerate to find the two numbers that add up to the target.
        We have a cache which will store the value and index of the number in the list. If the balance is in the cache
        then we return the index of the number and the index of the balance.
        """
        cache = {}
        for index, number in enumerate(numbers):
            key = target - number
            if key in cache:
                return [cache[key], index]
            cache[number] = index
        return []

    @staticmethod
    def two_sums_index_function(numbers: list[int], target: int) -> list[int]:
        """
        This method uses index function to find the two numbers that add up to the target.
        """
        for index, number in enumerate(numbers):
            balance = target - number
            if balance in numbers and balance != numbers[index]:
                return [index, numbers.index(balance)]
            elif balance in numbers[(index + 1) :] and balance == numbers[index]:
                numbers[index] = 0
                if balance == 0:
                    numbers[index] = 1
                return [index, numbers.index(balance)]
        return []


# @staticmethod
# def two_sums_solution_two():


if __name__ == "__main__":
    gen_list: list[int] = list(range(0, 10000))

    start = perf_counter()
    result_dual_for_loop = TwoSum.two_sums_solution_for_loop(numbers=gen_list, target=19999)
    print("Result with dual for loop", result_dual_for_loop)
    end = perf_counter()
    print(f"Time taken dual for loop: {end - start}")

    recursion_start = perf_counter()
    result_recursion = TwoSum.two_sums_recursion(numbers=gen_list, target=19997)
    print("Result with recursion", result_recursion)
    recursion_end = perf_counter()

    print(f"Time taken with recursion: {recursion_end - recursion_start}")

    enumerate_start = perf_counter()
    result_enumerate = TwoSum.two_sums_enumerate(numbers=[0, 4, 3, 0], target=0)
    print("Result with enumerate", result_enumerate)
    enumerate_end = perf_counter()

    print(f"Time taken with enumerate: {enumerate_end - enumerate_start}")

    index_start = perf_counter()
    result_index = TwoSum.two_sums_index_function(numbers=[0, 4, 3, 0], target=0)
    print("Result with index", result_index)
    index_end = perf_counter()

    print(f"Time taken with index: {index_end - index_start}")
