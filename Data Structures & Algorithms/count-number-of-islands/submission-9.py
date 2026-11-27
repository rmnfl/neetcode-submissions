class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(grid, r, c, visit):
            if min(r, c) < 0 or \
            r == ROWS or c == COLS or \
            (r, c) in visit or \
            grid[r][c] == "0":
                return 0

            visit.add((r, c))

            dfs(grid, r - 1, c, visit)
            dfs(grid, r + 1, c, visit)
            dfs(grid, r, c - 1, visit)
            dfs(grid, r, c + 1, visit)

            return 1

        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                count += dfs(grid, r, c, visit)

        return count