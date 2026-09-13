class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # uni=set()
        n=len(nums)
        i=0
        j=0
        while i < n:
            if(nums[i]!=nums[j]):
                # uni.add(nums[i])
                j+=1
                nums[j]=nums[i]
            else:
                i+=1

        return j+1