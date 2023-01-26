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

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        21. Merge Two Sorted Lists

        tail
        dummy -> null

                tail
        dummy -> 1 -> null      l1: 2 -> 4 -> null

                     tail
        dummy -> 1 -> 1 -> null     l2: 3 -> 4 -> null

                          tail
        dummy -> 1 -> 1 -> 2 -> null        l1: 4 -> null

        ...

        return dummy.next
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        141. Linked List Cycle
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    s = Solution()

    # head = [1, 2, 3, 4, 5]

    # nodes = []
    # nodes.append(ListNode(head[0]))
    # for i in range(1, len(head)):
    #     nodes.append(ListNode(head[i]))
    #     nodes[i - 1].next = nodes[i]

    # # # iterative
    # # rev = s.reverseList(nodes[0])
    # # print(rev, rev.next)

    # # recursive
    # rev = s.reverseListRecursive(nodes[0])
    # print(rev, rev.next)

    # l1 = [1, 2, 4]
    # l2 = [1, 3, 4]

    # nodes1, nodes2 = [], []

    # nodes1.append(ListNode(l1[0]))
    # for i in range(1, len(l1)):
    #     nodes1.append(ListNode(l1[i]))
    #     nodes1[i - 1].next = nodes1[i]

    # nodes2.append(ListNode(l2[0]))
    # for i in range(1, len(l2)):
    #     nodes2.append(ListNode(l2[i]))
    #     nodes2[i - 1].next = nodes2[i]

    # print(nodes1, nodes2)

    # r = s.mergeTwoLists(nodes1[0], nodes2[0])
    # while r:
    #     print(r)
    #     r = r.next

    head = [1, 2, 3, 4, 5]

    nodes = []
    nodes.append(ListNode(head[0]))
    for i in range(1, len(head)):
        nodes.append(ListNode(head[i]))
        nodes[i - 1].next = nodes[i]

    nodes[-1].next = nodes[1]
    print(s.hasCycle(nodes[0]))
