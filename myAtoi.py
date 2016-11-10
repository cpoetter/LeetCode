class Solution(object):
    
    def validNumber(self, number):
        validList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    
        valid = False
        for n in validList:
            if n == number:
                valid = True
                
        return valid
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        solution = 0
        negative = False
        count = 0
        
        for i in str:
            if self.validNumber(i):
                if i == '-':
                    negative = True
                else:
                    solution = solution * 10 + int(i)
                count = count + 1
            elif count == 0:
                pass
            else:
                break
        
        if negative == True:
            solution = solution * (-1)
            
        return solution

test = Solution()
print test.myAtoi("  +-1112   33")
