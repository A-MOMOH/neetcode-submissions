class Solution:
    def climbStairs(self, n: int) -> int:
        cur_step, next_step = 1, 2

        for i in range(1, n):
            cur_step, next_step = next_step, cur_step + next_step

        return cur_step