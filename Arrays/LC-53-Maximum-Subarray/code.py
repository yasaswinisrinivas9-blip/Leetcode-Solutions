class Solution:
    def maxSubArray(self, nums):

        summ = 0
        maxi = nums[0]

        for num in nums:

            summ += num

            if summ > maxi:
                maxi = summ

            if summ < 0:
                summ = 0

        return maxi