class Solution:
    def bin(self,arr,l,r,t):
        
        while l<=r:
            m=(l+r)//2
            if(arr[m]==t):
                return m
            elif(arr[m]>t):
                r=m-1
            else:
                l=m+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # print(self.bin1([0,1,2,4,5,6,7],6))
        # return

        n=len(nums)-1
        l,r=0,n
        res=0
        while l<=r:
            if(nums[r]>=nums[l]):
                if(nums[res]>nums[l]):
                    res=l
                break
            m=(l+r)//2
            if(nums[res]>nums[m]):
                res=m
            if(nums[m]>=nums[l]):
                l=m+1
            else:
                r=m-1
        if(target>=nums[res] and target<=nums[n]):
            return self.bin(nums,res,n,target)
        elif(target>=nums[0] and target<=nums[res-1]):
            return self.bin(nums,0,res-1,target)
        else:
            return -1
