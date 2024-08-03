# https://neetcode.io/problems/two-integer-sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            counter_part = target-nums[i]
            if counter_part in map:
                return [map.get(counter_part), i] 
            else:
                map[nums[i]] = i
        
if __name__ == "__main__":
    nums = [3,4,5,6]
    target = 7
    print(Solution().twoSum(nums, target))