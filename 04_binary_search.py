from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        704. Binary Search
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            # m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1


if __name__ == "__main__":
    s = Solution()

    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search([-1, 0, 3, 5, 9, 12], 2))
    print(s.search([5], 5))
    print(s.search([2, 5], 5))
