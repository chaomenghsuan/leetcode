from heapq import heapify, heappop, heappush

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            temp = n
            while temp % 2 == 0:
                temp //= 2
            heap.append((temp, max(n, temp*2)))
        
        heapify(heap)
        Max = max(i for i,j in heap)
        deviation = float('Inf')
        
        while len(heap) == len(nums):
            smallest, up_limit = heappop(heap)
            deviation = min(deviation, Max - smallest)
            if smallest < up_limit:
                heappush(heap, (smallest * 2, up_limit))
                Max = max(Max, smallest * 2)
        
        return deviation
