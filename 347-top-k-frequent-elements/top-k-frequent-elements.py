class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap={}
        # for i in range(k):
        #     myMap[i]=
        for i in range(len(nums)):
            if(nums[i] in myMap):
                myMap[nums[i]]+=1
            else:
                myMap[nums[i]]=1
        arr1=[]
        for n,f in myMap.items():
            arr1.append((f,n))
        arr1=sorted(arr1)
        return list(map(lambda t:t[1],arr1[-k:]))
