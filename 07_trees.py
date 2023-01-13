from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val} ({self.left.val}) ({self.right.val})"


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


if __name__ == "__main__":
    s = Solution()

    root = [4, 2, 7, 1, 3, 6, 9]  # Output: [4,7,2,9,6,3,1]

    n4 = TreeNode(4)
    n2, n7 = TreeNode(2), TreeNode(7)
    n4.left, n4.right = n2, n7

    n1, n3 = TreeNode(1), TreeNode(3)
    n2.left, n2.right = n1, n3

    n6, n9 = TreeNode(6), TreeNode(9)
    n7.left, n7.right = n6, n6

    # print(s.invertTree(n4))

    print(s.maxDepth_recursive(n4))
