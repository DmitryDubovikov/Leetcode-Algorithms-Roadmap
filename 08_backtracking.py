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

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        39. Combination Sum
        """
        result = []
        cur_kit = []
        cur_sum = 0

        def dfs(cur_kit, cur_sum, i):
            if cur_sum == target:
                result.append(cur_kit.copy())
                return
            if i >= len(candidates) or cur_sum > target:
                return

            # do include candidates[i]
            cur_kit.append(candidates[i])
            dfs(cur_kit, cur_sum + candidates[i], i)

            # do not include candidates[i]
            cur_kit.pop()
            dfs(cur_kit, cur_sum, i + 1)

        dfs(cur_kit, cur_sum, 0)

        return result


if __name__ == "__main__":
    s = Solution()

    # nums = [1, 2, 3]
    # print(s.subsets(nums))

    candidates = [2, 3, 6, 7]
    print(s.combinationSum(candidates, 7))
