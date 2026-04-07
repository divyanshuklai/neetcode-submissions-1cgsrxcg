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
            if (k, t, frozenset(used)) in memo:
                return False

            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    if backtrack(k, t - nums[i], used):
                        return True
                    used.remove(i)
            
            memo.add((k, t, frozenset(used)))
            return False
    
        return backtrack(k, target,  set())
            