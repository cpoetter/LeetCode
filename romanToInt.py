'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        conversion_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9 ,'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        solution = 0
        
        skip_next = False

        for i in range(len(s)):
            if skip_next == False:
                if s[i:i+2] in conversion_dict:
                    solution = solution + conversion_dict[s[i:i+2]]
                    skip_next = True
                else: 
                    solution = solution + conversion_dict[s[i:i+1]]
            else:
                skip_next = False        

        return solution

test = Solution()
print test.romanToInt("CDXXII")
