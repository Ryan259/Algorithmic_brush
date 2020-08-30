'''
1. Two Sum
description:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
import time
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finished = []
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    result = []
                    result.append(i)
                    result.append(k)
                    # print(result)
                    finished.append(result)
        return finished

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]

            d[target - nums[i]] = i

        return d


A = Solution()
nums = [2, 7, 2, 7]
target = 9
start = time.time()
result = A.twoSum(nums, target)
print(result)
print(f'first method cost time is {time.time() - start}')

start = time.time()
result2 = A.twoSum2(nums, target)

print(result2)
print(f'second method cost time is {time.time() - start}')

