class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        def map2d(x):
            i = x // N
            j = x % N

            return i, j

        l, r = 0, (M * N) - 1

        ans = None

        while l <= r:
            m = (l + r) // 2
            x, y = map2d(m)

            if matrix[x][y] < target:
                l = m + 1
            elif matrix[x][y] > target:
                r = m - 1
            else:
                return True
        
        return False