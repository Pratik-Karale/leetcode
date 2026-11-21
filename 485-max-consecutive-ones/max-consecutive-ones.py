class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr_count=0
        best=0
        for i in range(len(nums)):
            if(nums[i]==1):
                curr_count+=1
            if(nums[i]==0 or i==len(nums)-1):
                best=max(best,curr_count)
                curr_count=0
        return best
