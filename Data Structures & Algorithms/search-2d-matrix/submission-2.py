class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])

        l, r = 0, len(arr) - 1

        ans = None

        while l <= r:
            m = (l + r) // 2

            if arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                r = m - 1
            else:
                return True
        
        return False