# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        listLength = 0
        currentNode = head
        while currentNode != None:
            listLength = listLength + 1
            currentNode = currentNode.next
        
        if n == listLength:
            return head.next
        else:
            resultHead = head
            currentNode = head
            previousNode = None
            for i in range(listLength - n + 1):
                if i == (listLength - n):
                    previousNode.next = currentNode.next
                else:
                    previousNode = currentNode
                    currentNode = currentNode.next
                    
            return resultHead

test = Solution()
