# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         myMap={}
#         # for i in range(k):
#         #     myMap[i]=
#         for i in range(len(nums)):
#             if(nums[i] in myMap):
#                 myMap[nums[i]]+=1
#             else:
#                 myMap[nums[i]]=1
        
#         arr1=sorted(map(lambda x:(x[1],x[0]),myMap.items()))
#         return list(map(lambda t:t[1],arr1[-k:]))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res