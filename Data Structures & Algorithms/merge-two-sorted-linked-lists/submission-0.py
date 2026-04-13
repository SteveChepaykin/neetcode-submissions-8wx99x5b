# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 != None:
            return list2
        elif list2 == None and list1 != None:
            return list1
        elif list1 == None and list2 == None:
            return None
        c1 = list1
        c2 = list2
        tail = None
        out = None
        while c1 != None or c2 != None:
            if tail == None:
                if c2.val <= c1.val:
                    tail = ListNode(val=c2.val)
                    c2 = c2.next
                else:
                    tail = ListNode(val=c1.val)
                    c1 = c1.next
                out = tail
            else:
                if c1 == None:
                    tail.next = c2
                    c2 = c2.next
                elif c2 == None:
                    tail.next = c1
                    c1 = c1.next
                elif c2.val <= c1.val:
                    tail.next = c2
                    c2 = c2.next
                elif c2.val > c1.val:
                    tail.next = c1
                    c1 = c1.next
                tail = tail.next
        return out





