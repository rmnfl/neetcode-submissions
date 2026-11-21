class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high

        while low <= high:
            mid = (high + low) // 2

            total = sum([math.ceil(pile / mid) for pile in piles])

            if total > h:
                low = mid + 1
            else:
                result = mid
                high = mid - 1

        return result