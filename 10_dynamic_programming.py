from typing import List, Optional


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        70. Climbing Stairs
        """
        if n == 1:
            return 1
        cur, prev = 1, 1
        for _ in range(n - 1):
            cur, prev = cur + prev, cur
        return cur

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        746. Min Cost Climbing Stairs
        """
        cur, prev = 0, 0
        for c in cost[::-1]:
            cur, prev = c + min(cur, prev), cur
        return min(cur, prev)


if __name__ == "__main__":
    s = Solution()

    # print(s.climbStairs(5))

    # cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(s.minCostClimbingStairs(cost))
