# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        c = head
        if c == None:
            return False
        while c != None:
            if (c.val, c.next) in visited:
                return True
                break
            else:
                visited.append((c.val, c.next))
                c = c.next
        return False