class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        prefix[0] = 1
        suffix[n-1] = 1

        for i in range(1, n-1):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[n-1-i] = nums[n-1-i+1] * suffix[n-1-i+1]
        
        prefix[n-1] = prefix[n-2] * nums[n-2]
        suffix[0] = suffix[1] * nums[1]

        ret = []
        for i in range(n):
            ret.append(prefix[i] * suffix[i])

        return ret
