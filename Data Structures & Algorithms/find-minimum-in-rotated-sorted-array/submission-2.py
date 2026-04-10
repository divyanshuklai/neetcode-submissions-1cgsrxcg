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