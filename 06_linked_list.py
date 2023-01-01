from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        206. Reverse Linked List
        """
        # iterative solution
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


if __name__ == "__main__":
    s = Solution()

    s.reverseList([1, 2, 3, 4, 5])
    # print(s.reverseList(ListNode[1, 2, 3, 4, 5]))
    # print(s.reverseList(ListNode[1, 2]))
    # print(s.reverseList(ListNode[]))
