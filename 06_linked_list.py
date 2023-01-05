from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        206. Reverse Linked List
        """

        # iterative solution
        """
                1 -> 2 -> 3 -> 4 -> 5 -> None
        None <- 1    2 -> 3 -> 4 -> 5 -> None  
        prev   curr
        ...
        None <- 1 <- 2 <- 3 <- 4 <- 5 <- None
                                   prev  curr
        """
        prev, curr = None, head
        while curr:
            temp = curr.next  # save erased arrow
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    # recursive solution
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr: ListNode, prev: ListNode):
            if curr is None:
                return prev
            else:
                """
                        1 -> 2 -> 3 -> 4 -> 5 -> None
                None <- 1 -> 2 -> 3 -> 4 -> 5 -> None
                prev  curr  next
                """
                next = curr.next
                curr.next = prev
                return reverse(next, curr)

        return reverse(head, None)


if __name__ == "__main__":
    s = Solution()

    head = [1, 2, 3, 4, 5]

    nodes = []
    nodes.append(ListNode(head[0]))
    for i in range(1, len(head)):
        nodes.append(ListNode(head[i]))
        nodes[i - 1].next = nodes[i]

    # # iterative
    # rev = s.reverseList(nodes[0])
    # print(rev, rev.next)

    # recursive
    rev = s.reverseListRecursive(nodes[0])
    print(rev, rev.next)
