class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mi=prices[0]
        ma=0
        for i in range(len(prices)):
            mi=min(mi,prices[i])
            ma=max(ma,prices[i]-mi)
        return ma