# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        current = head
        for i in range(k):
            if not current:
                return head
            current = current.next
        
        prev = None
        current = head

        for i in range(k):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        if current:
            head.next = self.reverseKGroup(current, k)

        return prev

        # if k == 1:
        #     return head 

        # result = ListNode(next=head)

        # current = head
        # count = 0
        # while current:
        #     count += 1
        #     current = current.next

        # head, tail = result.next, result
        # # current = head
        # for _ in range(count // k):
        #     prev = None
        #     current = head
        #     for _ in range(k):
        #         head.next = prev
        #         prev = head
        #         head = head.next
        #     tail.next = prev
        #     tail = current

        