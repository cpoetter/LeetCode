'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            
            if l1.val <= l2.val:
                current_l1 = l1
                current_l2 = l2
                return_list = l1
            else:
                current_l1 = l2
                current_l2 = l1
                return_list = l2
            
            post_l1 = None
            post_l2 = None
            
            while current_l2 != None:
                while (current_l1 != None and current_l1.val <= current_l2.val):
                    post_l1 = current_l1
                    current_l1 = current_l1.next
                
                post_l1.next = current_l2
                temp_l2_next = current_l2.next
                current_l2.next = current_l1
                post_l1 = current_l2
                current_l2 = temp_l2_next
            
            return return_list
