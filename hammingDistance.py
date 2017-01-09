'''
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       |   |

The above arrows point to positions where the corresponding bits are different.
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        z = x^y
        length = len("{0:b}".format(z))
        distance = 0
        for i in range(length):
            distance += (z & (2**i)) >> i

        return distance


test = Solution()
print test.hammingDistance(x=1, y=4)
