from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        53. Maximum Subarray
        """
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)

        return max_sum


if __name__ == "__main__":
    s = Solution()

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, 1]

print(s.maxSubArray(nums))
