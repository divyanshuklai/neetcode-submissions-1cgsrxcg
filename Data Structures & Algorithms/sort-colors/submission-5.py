class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        f0 = f1 = f2 = n

        for i in range(n):
            if nums[i] == 0:
                if f1 < i:
                    nums[i], nums[f1] = nums[f1], nums[i]
                    if f1 < f0:
                        f0 = f1
                    if nums[f1+1] == 1:
                        f1 += 1
                    else:
                        f1 = i
                elif f2 < i:
                    nums[i], nums[f2] = nums[f2], nums[i]
                    if f2 < f0:
                        f0 = f2
                    if nums[f2+1] == 2:
                        f2+=1
                    else:
                        f2 = i
                elif i < f0:
                    f0 = i
            if nums[i] == 1:
                if f2 < i:
                    nums[i], nums[f2]  = nums[f2], nums[i]
                    if f2 < f1:
                        f1 = f2
                    if nums[f2+1] == 2:
                        f2 += 1
                    else:
                        f2 = i
                elif i < f1:
                    f1 = i
            if nums[i] == 2:
                if i < f2:
                    f2 = i