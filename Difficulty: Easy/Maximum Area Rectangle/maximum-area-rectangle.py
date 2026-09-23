class Solution:
    def calArea(self, arr):
        # Calculate area for each rectangle and return the maximum
        return max(l * b for l, b in arr)