"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        temp = head
        dct = {}
        while temp:
            dct[temp] = Node(x=temp.val)
            temp = temp.next

        current = head
        while current:
            dct[current].next = dct.get(current.next)
            dct[current].random = dct.get(current.random)
            current = current.next

        return dct.get(head, None)
        