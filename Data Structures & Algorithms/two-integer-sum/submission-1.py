class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()

        for i, num in enumerate(nums):
            if target - num in cache:
                return [cache[target - num], i]
            
            cache[num] = i