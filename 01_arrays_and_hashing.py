from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        217. Contains Duplicate
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.
        """
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        """
        242. Valid Anagram
        """
        if len(s) != len(t):
            return False

        dicts, dictt = {}, {}
        for i in range(len(s)):

            dicts[s[i]] = 1 + dicts.get(s[i], 0)
            dictt[t[i]] = 1 + dictt.get(t[i], 0)

        for key, value in dicts.items():
            if dictt.get(key) != value:
                return False

        return True

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Two Sum - return indices!
        """
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [i, seen[need]]
            else:
                seen[nums[i]] = i


if __name__ == "__main__":
    s = Solution()

    # print(s.containsDuplicate([1, 2, 3, 1]))

    # print(s.isAnagram("anagram", "nagaram"))
    # print(s.isAnagram("rat", "car"))

    # print(s.twoSum([2, 7, 11, 15], 9))
