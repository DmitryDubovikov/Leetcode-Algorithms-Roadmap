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


if __name__ == "__main__":
    s = Solution()

    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
