class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors=[0]*3
        for num in nums:
            colors[num]+=1
        j=0
        for c in range(len(colors)):
            for i in range(j,colors[c]+j):
                nums[i]=c
                j+=1
        