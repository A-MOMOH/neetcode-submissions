class Solution:
    def climbStairs(self, n: int) -> int:
        cur, next = 1, 2

        for i in range(1, n):
            cur, next = next, cur + next

        return cur