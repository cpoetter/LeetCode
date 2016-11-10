'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

import numpy as np

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution = []
        counter = 0
        for x in nums:
            y = target - x
            y_pos = np.where(np.asarray(nums) == y)[0]
            
            if y_pos.shape[0] > 0:
                if y_pos[0] != counter:
                    solution.append(counter)
                    solution.append(int(y_pos[0]))
                    break
            
            counter += 1
        return solution

test = Solution()
print test.twoSum([1, 3, 5], 8)
