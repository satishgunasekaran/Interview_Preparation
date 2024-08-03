# https://neetcode.io/problems/duplicate-integer

from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            if count_dict.get(num, None):
                return True
            count_dict[num] = 1
        return False
        

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().hasDuplicate(nums))