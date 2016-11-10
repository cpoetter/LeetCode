'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        parenthesis_list = []
        opening_parenthesis = ['(', '[', '{']
        closing_parenthesis = [')', ']', '}']
        
        for c in s:
            if c in opening_parenthesis:
                parenthesis_list.append(closing_parenthesis[opening_parenthesis.index(c)])
            elif c in closing_parenthesis:
                if len(parenthesis_list) != 0:
                    if c != parenthesis_list[-1]:
                        return False
                    else:
                        parenthesis_list.pop()
                else:
                    return False
            else:
                return False
                    
        if len(parenthesis_list) == 0:
            return True
        else:
            return False

test = Solution()
print test.isValid('([)')
