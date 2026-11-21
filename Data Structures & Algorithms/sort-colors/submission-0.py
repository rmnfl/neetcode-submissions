class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = {0: 0, 1: 0, 2: 0}

        for n in nums:
            buckets[n] += 1

        i = 0
        for k, v in buckets.items():
            for j in range(i, i + v):
                nums[j] = k
            i += v
