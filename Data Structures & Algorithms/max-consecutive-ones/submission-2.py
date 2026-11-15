class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        curr_consecutive = 0

        for n in nums:
            if n == 1:
                curr_consecutive += 1
            else:
                curr_consecutive = 0
                
            max_consecutive = max(max_consecutive, curr_consecutive)

        return max_consecutive