# # class Solution:
# #     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# #         myMap={}
# #         # for i in range(k):
# #         #     myMap[i]=
# #         for i in range(len(nums)):
# #             if(nums[i] in myMap):
# #                 myMap[nums[i]]+=1
# #             else:
# #                 myMap[nums[i]]=1
        
# #         arr1=sorted(map(lambda x:(x[1],x[0]),myMap.items()))
# #         return list(map(lambda t:t[1],arr1[-k:]))
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for num in nums:
#             count[num] = 1 + count.get(num, 0)
#         for num, cnt in count.items():
#             freq[cnt].append(num)

#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for num in freq[i]:
#                 res.append(num)
#                 if len(res) == k:
#                     return res

from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies using C-optimized Counter
        counts = Counter(nums)
        
        # 2. Group numbers by frequency using a hash map instead of a massive array
        freq_map = defaultdict(list)
        for num, freq in counts.items():
            freq_map[freq].append(num)
            
        # 3. Iterate backwards only from the maximum frequency found
        max_freq = max(freq_map.keys()) if freq_map else 0
        
        res = []
        for f in range(max_freq, 0, -1):
            if f in freq_map:
                res.extend(freq_map[f])
                if len(res) >= k:
                    return res[:k]
        return res