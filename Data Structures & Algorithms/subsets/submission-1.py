class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            for i in range(0, len(result)):
                sbset = result[i][:]
                sbset.append(num)
                result.append(sbset)
        
        return result