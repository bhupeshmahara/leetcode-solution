"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
NOTE : You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

# time O(n)
# space O(1)

import operator
from functools import reduce
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for number in nums:
            result = number ^ result
        return result


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in nums:
            if nums.count(x) == 1:
                return x

