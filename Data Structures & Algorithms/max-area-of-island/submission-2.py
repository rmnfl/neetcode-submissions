class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def dfs(r, c):
            if min(r, c) < 0 or \
            r == ROWS or c == COLS or \
            (r, c) in visit or \
            grid[r][c] == 0:
                return 0

            visit.add((r, c))

            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for i in range(ROWS):
            for j in range(COLS):
                maxArea = max(maxArea, dfs(i, j))

        return maxArea