class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        # pref = [0] * n
        # suff = [0] * n

        # pref[0] = suff[n - 1] = 1
        pref=1
        for i in range(1, n):
            res[i] = nums[i - 1] * pref
            pref=res[i]
        # print(res)
        suff=1
        for i in range(n - 2, -1, -1):
            res[i] = nums[i + 1] * suff * res[i]
            suff=nums[i + 1] * suff
        print(res)
        # for i in range(n):
        #     res[i] = pref[i] * suff[i]
        return res