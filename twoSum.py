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
