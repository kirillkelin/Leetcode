# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while lists and len(lists) > 1: 
            merge_lists = []
            for i in range(0, len(lists), 2):
                list_left = lists[i]
                list_right = lists[i+1] if i+1 < len(lists) else None
                merge_lists.append(self.mergeTwoLists(list_left, list_right))
            lists = merge_lists
        
        return lists[0]

    
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return list1
        
        if not list1 or not list2:
            return list2 if not list1 else list1

        result = list1 if list2.val >= list1.val else list2

        while list1 and list2:
            if list2.val >= list1.val:
                while list1.next and list1.next.val <= list2.val:
                    list1 = list1.next
                list1.next, list1 = list2, list1.next
                # prev = list1.next
                # list1.next = list2
                # list1 = prev
            else:
                while list2.next and list2.next.val <= list1.val:
                    list2 = list2.next
                list2.next, list2 = list1, list2.next
                # prev = list2.next
                # list2.next = list1
                # list2 = prev
        return result

