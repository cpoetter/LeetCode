class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        solution = ""
        counter = 0
        
        for current_string in strs:
            if counter == 0:
                solution = current_string
            else:
                another_counter = 0
                for chrs in solution:
                    if another_counter < len(current_string):
                        if chrs != current_string[another_counter]:
                            solution = solution[0:another_counter]
                            break
                        another_counter = another_counter + 1
                    else:
                        solution = solution[0:another_counter]
                        break
            counter = counter + 1 
        return solution

test = Solution()
print test.longestCommonPrefix(['aa', 'a', 'aatess'])
