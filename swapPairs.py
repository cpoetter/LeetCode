'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head
        elif head.next == None:
            return head
        else:
            solution_head = head.next
            
            current_node = head
            previous_node = None
            while current_node != None:
                a = current_node
                b = current_node.next
                
                if b != None: 
                    c = b.next
                    b.next = a
                    a.next = c
                    
                    if previous_node != None:
                        previous_node.next = b
                    
                    current_node = c
                    previous_node = a
                else:
                    break
                
            return solution_head
