class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        minHeap = []
        for x, y in points:
            minHeap.append((x ** 2 + y ** 2, x, y,))

        heapq.heapify(minHeap)

        for _ in range(k):
            dits, x, y = heapq.heappop(minHeap)
            result.append([x, y])

        return result