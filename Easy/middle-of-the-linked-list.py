import math

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):

        nodes = []

        while head:
            nodes.append(head)
            head = head.next
        
        middle = int(math.ceil(len(nodes)//2))
        n = nodes[middle]

        return n