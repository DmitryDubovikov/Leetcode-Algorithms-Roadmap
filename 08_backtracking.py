from typing import List, Optional


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        78. Subsets
        """
        result = []
        subset = []

        def dfs(n):

            if n == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[n])
            dfs(n + 1)

            subset.pop()
            dfs(n + 1)

        dfs(0)

        return result


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3]
    print(s.subsets(nums))
