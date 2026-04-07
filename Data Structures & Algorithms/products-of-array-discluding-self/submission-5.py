class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot  = 1
        num_zeros = 0
        zero_idx = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros+=1
                zero_idx = i
                continue
            tot *= nums[i]
        prod = [0] * len(nums)
        if num_zeros > 1:
            return prod
        elif num_zeros == 1:
            prod[zero_idx] = tot
            return prod
        for i in range(len(nums)):
            prod[i] = tot//nums[i]
        return prod