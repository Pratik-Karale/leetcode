class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        maxAr=0
        while(l<r):
            ar=(r-l)*min(height[l],height[r])
            if(ar>maxAr):
                    maxAr=ar
            if(height[l]<=height[r]):
                l+=1
            else:
                r-=1
        return maxAr


        pref=[i*j for i,j in enumerate(height)]
        for i in range(n):
            j=n-1
            while(i<j):
                if(height[i]>height[j]):
                    ar=pref[j]-height[i]*i
                else:
                    ar=pref[i]-height[j]*j
                if(ar>maxAr):
                    # print(j,height[j],i,height[i])
                    maxAr=ar
                j-=1
        return maxAr

        maxL=l
        maxR=r
        while(l<r):
            
            l+=1
            r-=1
