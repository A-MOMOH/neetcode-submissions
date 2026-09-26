class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        index = 0
        sum_list = []
        
        while index < n - 1:
            for i in range(index + 1, n):
                if nums[i] == target - nums[index]:
                    sum_list.append(index)
                    sum_list.append(i)
            
            index += 1
        
        return sum_list