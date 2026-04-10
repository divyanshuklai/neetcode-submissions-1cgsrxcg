class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        res = 1001
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[end]:
                if  res < nums[mid]:
                    return res 
                res = nums[mid]
                end = mid - 1
            else:
                start = mid + 1
        return res

# 0 1 2 3 4 5 
# 4 5 6 7
# mid = 0 + (3-0)/2 = 1, nums[mid=1] = 5, nums[end=3]=7, end = 0
# mid = 0 + (0-0)//2 = 0, nums[mid=0] = 4, nums[end]