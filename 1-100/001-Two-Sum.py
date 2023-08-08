from typing import List

# time O(n)
# space O(1)


class Solution(object):
    def twoSum(self, nums, target):
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if target - n in nums and i != nums.index(target - n):
                return i, nums.index(target - n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while nums:
            k = len(nums)-1
            n = nums.pop()            
            if (target-n) in nums:
                return [k, nums.index(target-n)]


# time O(n^2)
# space O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if( nums[i] + nums[j] == target):
                    return [i, j]
