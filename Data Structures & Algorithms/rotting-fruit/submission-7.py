class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        fresh, rotten = 0, 0
        result = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc

                    if (
                        min(nr, nc) < 0 or 
                        nr == ROWS or nc == COLS or 
                        (nr, nc) in visit or 
                        grid[nr][nc] == 0
                    ):
                        continue
                    
                    queue.append((nr, nc))
                    visit.add((nr, nc))
                    fresh -= 1

            result += 1

        if not fresh:
            return result

        return -1

