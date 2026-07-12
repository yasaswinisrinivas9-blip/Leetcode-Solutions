class Solution:
    def arrayRankTransform(self, arr):

        sorted_arr = sorted(set(arr))

        r = 1
        rank = {}

        for num in sorted_arr:
            rank[num] = r
            r += 1

        return [rank[num] for num in arr]


       