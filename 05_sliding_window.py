from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        121. Best Time to Buy and Sell Stock
        """
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            elif prices[l] > prices[r]:
                l = r
            r += 1

        return max_profit

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters
        """
        max_len = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len


if __name__ == "__main__":
    s = Solution()

    # print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    # print(s.maxProfit([7, 6, 4, 3, 1]))

    st = "pwwkewwwpotr"
    print(s.lengthOfLongestSubstring(st))
