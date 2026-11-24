class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        print(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)

            if s1 != s2:
                heapq.heappush(stones, s1 - s2)

        if stones:
            return -stones[0]
        
        return 0
        
        