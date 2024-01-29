# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        stack = []
        temp = head
        result = head

        while head:
            stack.append(head)
            head = head.next

        while temp:
            cur = temp.next
            nxt_stack = stack.pop()
            if cur == nxt_stack:
                temp.next = nxt_stack
                nxt_stack.next = None
                break
            elif temp == nxt_stack:
                temp.next = None
                break
            else:
                temp.next = nxt_stack
                nxt_stack.next = cur
            temp = cur

        return result
            
