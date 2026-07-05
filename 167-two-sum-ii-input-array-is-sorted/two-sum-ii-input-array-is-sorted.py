class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while(l<r):
            TwoSum=numbers[l]+numbers[r]
            if(TwoSum>target):
                r-=1
            elif(TwoSum<target):
                l+=1
            else:
                return [l+1,r+1]
            while(l>0 and numbers[l-1]==numbers[l]):
                l+=1
        return []