class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        input_number = str(x)
        solution = []
        negative = False

        for i in input_number:
            if i != '-':
                solution.insert(0, i)
            else:
                negative = True

        if negative == True:
            solution.insert(0, '-')

        return int(''.join(solution))

test = Solution()
print test.reverse(-123)
