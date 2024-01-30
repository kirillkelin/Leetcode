# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        value = 0

        while l1 or l2:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            temp = l1_value + l2_value + value
            value = 0
            if temp > 9:
                temp = temp % 10
                value += 1
            current.val = temp
            current.next = ListNode(val = value)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None and current.next.val == 0:
                current.next = None
            else:
                current = current.next
        
        return head