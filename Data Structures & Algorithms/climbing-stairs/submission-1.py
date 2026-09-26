class Solution:
    def climbStairs(self, n: int) -> int:
        cur, prev = 1, 1

        for i in range(1, n):
            cur, prev = cur + prev, cur

        return cur