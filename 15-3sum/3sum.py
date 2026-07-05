# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         n=len(nums)
#         res=[]
#         nums=sorted(nums)
#         mp=defaultdict(int)
#         for num in nums:
#             mp[num]+=1
#         for i in range(n):
#             mp[i]-=1
#             if(i>0 and nums[i-1]==nums[i]):
#                 continue
#             for j in range(i+1,n):
#                 mp[j]-=1
#                 if(j>i+1 and nums[j-1]==nums[j]):
#                     continue
#                 target=-(nums[i]+nums[j])
#                 if(mp[target]>0):
#                     res.append([nums[i],nums[j],target])
#             for j in range(i+1,n):
#                 mp[j]+=1
#         return res

#         # for i,num in enumerate(hs):
#         #     # sum=num
#         #     for j,num2 in enumerate(hs[i+1:]):
#         #         if(num+num2 in hs[j+1:] and sorted([num,num2,num+num2]))

            
#         n=len(nums)
#         res=[]
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     if(nums[i]+nums[j]+nums[k]==0):
#                         item=sorted([nums[i],nums[j],nums[k]])
#                         if(item in res):
#                             continue
#                         res.append(item)
#         return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res