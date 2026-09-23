class Solution:
    def distance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        # code here
        return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5)