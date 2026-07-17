class Solution:
    def majorityElement(self,nums):
        
        n = len(nums)
        
        cnt1,cnt2 =0,0
        ele1,ele2 = None,None
        
        
        for num in nums:
            
            if cnt1 == 0 and num != ele2:
                ele1 = num
                cnt1 = 1
                
            elif cnt2 == 0 and num !=  ele1:
                ele2 = num
                cnt2 = 1
                
            elif num == ele1:
                cnt1 += 1
                
            elif num == ele2:
                cnt2 += 1
            
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        cnt1, cnt2 =0,0
        
        for num in nums:
            
            if num == ele1:
                cnt1 += 1
                
            elif num == ele2:
                cnt2 += 1
                
        ans = []
        
        if cnt1 > n // 3:
            ans.append(ele1)
            
        if cnt2 > n // 3:
            ans.append(ele2)
            
        return ans
    



        