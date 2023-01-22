from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        226. Invert Binary Tree
        """
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        """
        104. Maximum Depth of Binary Tree
        """
        if not root:
            return 0
        return 1 + max(
            self.maxDepth_recursive(root.left), self.maxDepth_recursive(root.right)
        )

    def maxDepth_deque(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            level += 1
        return level

    def maxDepth_stack(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        max_level = 1

        while stack:
            node, depth = stack.pop()

            if node:
                max_level = max(max_level, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return max_level

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        543. Diameter of Binary Tree
        """

        diameter = 0

        def dfs(root):
            nonlocal diameter

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(diameter, left + right)

            return max(left, right) + 1

        dfs(root)

        return diameter

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        110. Balanced Binary Tree
        """
        balanced = True

        def maxDepth(node: Optional[TreeNode]) -> bool:
            nonlocal balanced
            if not node:
                return 0
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            if abs(left_depth - right_depth) > 1:
                balanced = False
            return 1 + max(left_depth, right_depth)

        maxDepth(root)
        return balanced

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        100. Same Tree
        """
        if not p and not q:
            return True
        elif (not p or not q) or (p.val != q.val):
            return False
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))


if __name__ == "__main__":
    s = Solution()

    root = [4, 2, 7, 1, 3, 6, 9]  # Output: [4,7,2,9,6,3,1]

    n4 = TreeNode(4)
    n2, n7 = TreeNode(2), TreeNode(7)
    n4.left, n4.right = n2, n7

    n1, n3 = TreeNode(1), TreeNode(3)
    n2.left, n2.right = n1, n3

    n6, n9 = TreeNode(6), TreeNode(9)
    n7.left, n7.right = n6, n9

    # print(s.invertTree(n4))

    # print(s.maxDepth_recursive(n4))
    # print(s.maxDepth_deque(n4))
    # print(s.maxDepth_stack(n4))
    # print(s.diameterOfBinaryTree(n4))
    # print(s.isBalanced(n4))
    print(s.isSameTree(n4, n4))
