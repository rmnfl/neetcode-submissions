class Solution:
    cache = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            if n in self.cache:
                return self.cache[n]
            else:
                result = self.climbStairs(n - 1) + self.climbStairs(n-2)
                self.cache[n] = result
                return result