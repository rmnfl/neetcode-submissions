class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            currSum = sum(subset)

            if i >= len(nums) or currSum > target:
                return 
            
            if currSum == target:
                result.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)

        dfs(0)

        return result