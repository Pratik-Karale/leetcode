class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        s=set()
        for num in  nums:
            s.add(num)
        i=1
        while True:
            if(i not in s):
                return i
            i+=1