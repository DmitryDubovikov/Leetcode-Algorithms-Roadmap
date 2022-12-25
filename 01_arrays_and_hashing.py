from typing import List


class Solution:
    
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        217. Contains Duplicate
        Given an integer array nums, return true if any value appears at least twice in the array, 
        and return false if every element is distinct.
        '''
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False




if __name__ == '__main__':
    s = Solution()

    print(s.containsDuplicate([1,2,3,1]))

