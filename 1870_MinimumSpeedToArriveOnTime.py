from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist)-1:
            return -1
        left = 1
        right = max(dist) * 100 # which is max(dist)/0.01
        while left < right:
            v = (left + right) // 2
            t = sum([ceil(dist[i]/v) if i != len(dist)-1 else dist[i]/v for i in range(len(dist))])
            if t > hour:
                left = v + 1
            else:
                right = v
        if left > max(dist) * 100:
            return -1
        else:
            return left
