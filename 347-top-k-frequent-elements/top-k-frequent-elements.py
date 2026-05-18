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
        
        arr1=sorted(map(lambda x:(x[1],x[0]),myMap.items()))
        return list(map(lambda t:t[1],arr1[-k:]))
