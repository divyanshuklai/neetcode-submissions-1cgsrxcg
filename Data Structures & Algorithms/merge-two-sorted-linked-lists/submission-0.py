# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = head
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                if head is None:
                    head = list1
                    cur = head
                else:
                    cur.next = list1
                    cur = cur.next
                list1 = list1.next
            else:
                if head is None:
                    head = list2
                    cur = head
                else:
                    cur.next = list2
                    cur = cur.next
                list2 = list2.next
            
        
        if list1 is not None:
            if head is None:
                return list1
            else:
                cur.next  = list1

        if head is not None:
            while cur.next is not None:
                cur = cur.next
        
        if list2 is not None:
            if head is None:
                return list2
            else:
                cur.next = list2

        return head


                

