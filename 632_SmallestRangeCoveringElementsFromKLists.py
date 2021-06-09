import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)

        low, high = -float('Inf'), float('Inf')
        right = max([row[0] for row in nums])
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < high - low:
                high, low = right, left
            if j+1 == len(nums[i]):
                return [low, high]
            right = max(right, nums[i][j+1])
            heapq.heappush(pq, (nums[i][j+1], i, j+1))
