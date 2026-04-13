# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        p_c1 = None
        c1 = head
        c2 = head
        while c2 and c2.next:
            p_c1 = c1
            c1 = c1.next
            c2 = c2.next.next
        p_c1.next = None

        prev = None
        cur = c1
        while cur != None:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex

        cfirst = head
        csecond = prev
        while csecond != None:
            temp1 = cfirst.next
            temp2 = csecond.next
            if temp1 != None:
                cfirst.next = csecond
                csecond.next = temp1
                cfirst = temp1
                csecond = temp2
            else:
                cfirst.next = csecond
                csecond.next = temp2
                break

            
                
