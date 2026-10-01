import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_list = [1] * n

        prefix = 1
        for i in range(n):
            product_list[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            product_list[i] *= suffix
            suffix *= nums[i]

        return product_list