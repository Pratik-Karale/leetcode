class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i=0
        # j=0
        # while i<len(nums):
        #     if(nums[j]!=val):
        #         j+=1
        #     elif(nums[j]==val and nums[i]!=val):
        #         nums[j]=nums[i]
        #         # j+=1
        #     i+=1
        # return j
        j=0
        for i in range(len(nums)):
            if(nums[j]==val and nums[i]!=val):
                nums[j],nums[i]=nums[i],nums[j]
            if(nums[j]!=val):
                j+=1
        return j

        