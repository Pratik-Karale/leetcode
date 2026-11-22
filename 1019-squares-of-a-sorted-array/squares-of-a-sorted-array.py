class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i]**=2
        l=0
        r=len(nums)-1
        res=[]
        while l<=r:
            if(nums[l]>nums[r]):
                res.append(nums[l])
                l+=1
            else:
                res.append(nums[r])
                r-=1
        return res[::-1]