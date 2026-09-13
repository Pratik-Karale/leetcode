class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # uni=set()
        n=len(nums)
        i=0
        j=0
        while i < n:
            if(nums[i] not in nums[:j]):
                # uni.add(nums[i])
                nums[j]=nums[i]
                j+=1
            else:
                i+=1

        return j