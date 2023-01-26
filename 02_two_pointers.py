from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        125. Valid Palindrome
        """
        l, r = 0, len(s) - 1

        while l < r:

            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        167. Two Sum II - Input Array Is Sorted
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return [l + 1, r + 1]


if __name__ == "__main__":
    s = Solution()

    # print(s.isPalindrome("A man, a plan, a canal: Panama"))
    # print(s.isPalindrome("race a car"))
    # print(s.isPalindrome("0P"))
    # print(s.isPalindrome(" "))

    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers, target))
