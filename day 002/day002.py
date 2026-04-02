# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        dumb = ListNode()
        current = dumb
        carry = 0

        while l1 or l2 or carry:          

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum1 = val1 + val2 + carry 

            current.val = sum1%10
            carry = sum1//10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            current.next = ListNode() if l1 or l2 or carry else None
            current = current.next if l1 or l2 or carry else current

        return dumb