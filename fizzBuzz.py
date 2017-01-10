"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz". For numbers which are multiples of both three and five output "FizzBuzz".

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = range(1, n+1)
        result = map(str, result)
        result[2::3] = ['Fizz']*len(result[2::3])
        result[4::5] = ['Buzz']*len(result[4::5])
        result[14::15] = ['FizzBuzz']*len(result[14::15])

	return result

test = Solution()
print test.fizzBuzz(15)
