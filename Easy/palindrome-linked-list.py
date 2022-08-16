import math

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        
        if head is None:
            return
        
        temp = []
        n = head
        
        while n:
            temp.append(n.val)
            n = n.next
            
        if temp == temp[::-1]:
            return True
        else:
            return False