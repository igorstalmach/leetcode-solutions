# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = []
        num2 = []

        while l1:
            num1.append(l1.val)
            l1 = l1.next

        while l2:
            num2.append(l2.val)
            l2 = l2.next

        num1 = int(''.join(list(map(str, num1[::-1]))))
        num2 = int(''.join(list(map(str, num2[::-1]))))
        num3 = num1 + num2
        num3 = str(num3)[::-1]

        n = ListNode()
        out = n

        for i in range(len(num3)-1):
            n.val = int(num3[i])
            n.next = ListNode()
            n = n.next
        n.val = int(num3[-1])

        return out