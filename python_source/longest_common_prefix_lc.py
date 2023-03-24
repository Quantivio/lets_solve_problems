# Leet Code Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Complexity: Easy
# Description: Write a function to find the longest common prefix string amongst an array of strings.


"""
Example:
    Input: ["flower","flow","flight"]
    Output: "fl"
    Explanation: The longest common prefix is "fl".
"""


class LongestCommonPrefix:
    @staticmethod
    def solution(strings: list[str]):
        """
        This method will return the longest common prefix string amongst an array of strings.
        """
        if not strings:
            return ""
        prefix = strings[0]
        for index in range(1, len(strings)):
            while strings[index].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


if __name__ == "__main__":
    print(LongestCommonPrefix.solution(["dog", "racecar", "car"]))
