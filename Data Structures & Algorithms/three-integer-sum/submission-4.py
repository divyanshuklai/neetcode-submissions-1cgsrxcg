from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort(reverse=True)

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    res.add(
                        (nums[right], nums[left], nums[i])
                    )
                if sum >= 0:
                    left+=1
                else:
                    right-=1

        return list(res)