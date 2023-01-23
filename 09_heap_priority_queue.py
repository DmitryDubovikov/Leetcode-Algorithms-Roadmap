from typing import List
import heapq


class KthLargest:
    """
    703. Kth Largest Element in a Stream
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        1046. Last Stone Weight
        """
        stones = [-s for s in stones]  # we don't have maxHeap in python
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:  # we made weights negative
                heapq.heappush(stones, first - second)

        if len(stones) == 0:
            return 0
        return abs(stones[0])


# kthLargest = KthLargest(3, [4, 5, 8, 2])
# # return 4
# print(kthLargest.add(3))
# # return 5
# print(kthLargest.add(5))
# # return 5
# print(kthLargest.add(10))
# # return 8
# print(kthLargest.add(9))
# # return 8
# print(kthLargest.add(4))


if __name__ == "__main__":
    s = Solution()

    stones = [2, 7, 4, 1, 8, 1]
    print(s.lastStoneWeight(stones))
