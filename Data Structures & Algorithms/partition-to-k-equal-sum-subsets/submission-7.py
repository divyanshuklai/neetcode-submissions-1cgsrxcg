class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k != 0:
            return False
        
        target  = sum(nums)//k

        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        memo = set()
        def backtrack(k, t, used):
            if k == 0:
                return True
            if t == 0:
                return backtrack(k-1, target, used)
            if t < 0:
                return False
            if (k, t, used) in memo:
                return False

            for i in range(len(nums)):
                if used & 1 << i == 0:
                    used |= 1 << i
                    if backtrack(k, t - nums[i], used):
                        return True
                    used &= ~(1 << i)
            
            memo.add((k, t, used))
            return False
    
        return backtrack(k, target, 0)
            