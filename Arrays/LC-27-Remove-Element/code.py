#Optimal Approach

class Solution:
    def removeElement(self,arr,val):
        
        #k is Write Pointer
        k = 0
        #i is Read Pointer
        for i in range(len(arr)):
            if arr[i] != val:
                arr[k] = arr[i] 
                #Update K if that i element is not equal to val
                
                k += 1
                
        return k
    

sol = Solution()
print(sol.removeElement([3,2,2,3], 3))