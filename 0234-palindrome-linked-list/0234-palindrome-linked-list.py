# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        newHead = self.reverse(slow.next)
        first = head
        second = newHead
        while(second is not None ):
            if first.val is not second.val:
                self.reverse(newHead)
                return False
            else:
                first = first.next
                second = second.next

        self.reverse(newHead)
        return True