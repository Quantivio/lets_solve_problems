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
