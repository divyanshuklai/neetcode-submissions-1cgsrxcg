class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            elif nums[i] == 2:
                two += 1
        
        idx=0
        while zero != 0:
            nums[idx]=0
            idx+=1
            zero-=1
        while one != 0:
            nums[idx]=1
            idx+=1
            one-=1
        while two != 0:
            nums[idx]=2
            idx+=1
            two-=1

           



# 1 1 0 2 1 0 0
#   
