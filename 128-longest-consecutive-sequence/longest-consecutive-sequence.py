class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        m=0
        for num in numSet:
            if(num-1 in numSet):
                continue
            length=1
            while(num+length in numSet):
                length+=1
            if(length>m):
                m=length
        return m
        