"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x,
such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

# time O(n)
# space O(n)

from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        return str1[:gcd(len(str1), len(str2))]


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        elif str1 == str2:
            return str1
        elif str1[:len(str2)] != str2:
            return ""
        return self.gcdOfStrings(str1[len(str2):], str2)


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        elif str1 == str2:
            return str1
        elif (str1 + str2) != (str2 + str1):
            return ""
        return self.gcdOfStrings(str1[len(str2):], str2)


