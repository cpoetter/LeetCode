'''

Given a binary array, find the maximum number of consecutive 1s in this array.

Example

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        consecutive = 0
        max_consecutive = 0
        for i in nums:
            if i == 1:
                consecutive += 1
            else:
                if consecutive > max_consecutive:
                    max_consecutive = consecutive
                consecutive = 0

        if consecutive > max_consecutive:
            max_consecutive = consecutive

        return max_consecutive

test = Solution()
print test.findMaxConsecutiveOnes([1, 0, 1, 1, 1, 0, 0, 1, 1])
