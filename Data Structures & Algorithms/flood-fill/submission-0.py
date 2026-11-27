class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])

            if min(r, c) < 0 or \
            r == ROWS or c == COLS or \
            (r, c) in visit or \
            grid[r][c] != grid[sr][sc]:
                return
            
            visit.add((r, c))
            
            dfs(grid, r + 1, c, visit)
            dfs(grid, r - 1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c - 1, visit)

            grid[r][c] = color

        dfs(image, sr, sc, set())

        return image