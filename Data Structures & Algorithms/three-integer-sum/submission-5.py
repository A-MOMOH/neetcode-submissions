class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_dict = {}
        n = len(nums)
        sum_set = set()

        for i, v in enumerate(nums):
            sum_dict[v] = i
            
        
        for i in range(n):
            for j in range(i + 1, n):

                needed = -(nums[i] + nums[j])
                k = sum_dict.get(needed)

                if k is not None and k != i and k != j:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    sum_set.add(triplet)

        # Convert set of tuples to list of lists
        return [list(x) for x in sum_set]