class Solution:
    def highestAltitude(self,gain):
        
        altitude = 0
        highest = 0
        
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
            
        return highest


sol = Solution()
print(sol.highestAltitude([-5,1,5,0,-7]))